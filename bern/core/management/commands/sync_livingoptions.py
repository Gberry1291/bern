from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from parler.utils.context import switch_language

from core.models import Provider, LivingOption

# IMPORTANT: import your dataset
from core.seed_data.model_data import MODEL_DATA


@dataclass(frozen=True)
class Key:
    provider_id: int
    slug: str


def _norm_bool(v: Any) -> bool:
    return bool(v)


def _norm_int(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except Exception:
        return default


def _norm_list(v: Any) -> list:
    if v is None:
        return []
    if isinstance(v, list):
        return v
    return list(v)


def _same(a: Any, b: Any) -> bool:
    # JSONField list ordering matters; if you want order-insensitive, sort here.
    return a == b


class Command(BaseCommand):
    help = "Sync LivingOption rows from MODEL_DATA (create/update + delete missing)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Actually write changes. Without this flag it's a dry-run.",
        )
        parser.add_argument(
            "--delete-missing",
            action="store_true",
            default=True,
            help="Delete DB LivingOptions not present in MODEL_DATA (default: on).",
        )
        parser.add_argument(
            "--no-delete-missing",
            action="store_true",
            help="Disable deletion of missing rows.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Only process first N dataset items (0 = all).",
        )

    @transaction.atomic
    def handle(self, *args, **opts):
        apply = bool(opts["apply"])
        limit = int(opts["limit"] or 0)

        delete_missing = bool(opts["delete_missing"]) and not bool(opts["no_delete_missing"])

        items = MODEL_DATA[:limit] if limit else MODEL_DATA

        # Disable embedding signals during sync to avoid API spam
        old_disable = getattr(settings, "DISABLE_EMBEDDING_SIGNALS", False)
        setattr(settings, "DISABLE_EMBEDDING_SIGNALS", True)

        try:
            # Build provider list in a stable order by ID
            providers = list(Provider.objects.all().order_by("id"))
            if not providers:
                raise RuntimeError("No Provider rows found. Seed providers first.")

            # Track desired keys so we can delete missing
            desired_keys: set[Key] = set()
            providers_touched: set[int] = set()

            created = 0
            updated = 0
            unchanged = 0

            for idx, d in enumerate(items, start=1):
                provider_idx = d.get("provider_idx")
                slug = (d.get("slug") or "").strip()
                if provider_idx is None or slug == "":
                    raise RuntimeError(f"Bad dataset row #{idx}: missing provider_idx or slug")

                try:
                    provider = providers[int(provider_idx)]
                except Exception:
                    raise RuntimeError(f"Bad provider_idx={provider_idx} in dataset row #{idx}")

                providers_touched.add(provider.id)
                key = Key(provider_id=provider.id, slug=slug)
                desired_keys.add(key)

                # Structured fields from dataset
                incoming = {
                    "care_level": _norm_int(d.get("care_level")),
                    "cognitive_support_level": _norm_int(d.get("cognitive_support_level")),
                    "wheelchair_accessible": _norm_bool(d.get("wheelchair_accessible")),
                    "hearing_support": _norm_bool(d.get("hearing_support")),
                    "visual_support": _norm_bool(d.get("visual_support")),
                    "languages_supported": _norm_list(d.get("languages_supported")),
                    "min_age": _norm_int(d.get("min_age"), default=0),
                    "max_age": _norm_int(d.get("max_age"), default=120),
                }

                translations = d.get("translations") or {}

                lo = LivingOption.objects.filter(provider=provider, slug=slug).first()
                if lo is None:
                    if apply:
                        lo = LivingOption(provider=provider, slug=slug, **incoming)
                        lo.save()
                        # translations
                        for lang, tdata in translations.items():
                            title = (tdata.get("title") or "").strip()
                            desc = (tdata.get("description") or "").strip()
                            if not (title or desc):
                                continue
                            with switch_language(lo, lang):
                                if title:
                                    lo.title = title
                                if desc:
                                    lo.description = desc
                                lo.save()
                    created += 1
                    continue

                # Compare + update structured fields
                dirty_fields: list[str] = []
                for f, v in incoming.items():
                    if not _same(getattr(lo, f), v):
                        setattr(lo, f, v)
                        dirty_fields.append(f)

                # Compare + update translations (only if different)
                dirty_translations = 0
                for lang, tdata in translations.items():
                    new_title = (tdata.get("title") or "").strip()
                    new_desc = (tdata.get("description") or "").strip()
                    if not (new_title or new_desc):
                        continue

                    old_title = lo.safe_translation_getter("title", language_code=lang, any_language=False) or ""
                    old_desc = lo.safe_translation_getter("description", language_code=lang, any_language=False) or ""

                    if new_title != old_title or new_desc != old_desc:
                        dirty_translations += 1
                        if apply:
                            with switch_language(lo, lang):
                                if new_title:
                                    lo.title = new_title
                                if new_desc:
                                    lo.description = new_desc
                                lo.save()

                if dirty_fields or dirty_translations:
                    updated += 1
                    if apply and dirty_fields:
                        lo.save(update_fields=dirty_fields)
                else:
                    unchanged += 1

            # Delete missing rows (only for providers touched by this dataset)
            deleted = 0
            if delete_missing:
                # For each provider we touched, compute expected slugs and delete others
                for pid in providers_touched:
                    expected_slugs = {k.slug for k in desired_keys if k.provider_id == pid}
                    qs = LivingOption.objects.filter(provider_id=pid).exclude(slug__in=expected_slugs)
                    count = qs.count()
                    if count:
                        if apply:
                            qs.delete()
                        deleted += count

            self.stdout.write("")
            self.stdout.write(self.style.SUCCESS("Sync summary"))
            self.stdout.write(f"  Created:   {created}")
            self.stdout.write(f"  Updated:   {updated}")
            self.stdout.write(f"  Unchanged: {unchanged}")
            self.stdout.write(f"  Deleted:   {deleted if delete_missing else 0} ({'enabled' if delete_missing else 'disabled'})")

            if not apply:
                self.stdout.write("")
                self.stdout.write(self.style.WARNING("DRY-RUN ONLY. Re-run with --apply to write changes."))

        finally:
            setattr(settings, "DISABLE_EMBEDDING_SIGNALS", old_disable)
