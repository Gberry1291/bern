from __future__ import annotations
from pathlib import Path
import json
from django.core.management.base import BaseCommand
from pprint import pformat
from core.models import Provider, LivingOption


class Command(BaseCommand):
    help = "Export LivingOption rows (including Parler translations) as a human-readable Python dict list."

    def add_arguments(self, parser):
        parser.add_argument(
            "--pretty-json",
            action="store_true",
            help="Output JSON instead of a Python literal list.",
        )
        parser.add_argument(
            "--include-provider-name",
            action="store_true",
            help="Include provider_name for readability (recommended).",
        )

    def handle(self, *args, **opts):
        pretty_json = opts["pretty_json"]
        include_provider_name = opts["include_provider_name"]

        providers = list(Provider.objects.all().order_by("id"))
        provider_idx_by_id = {p.id: i for i, p in enumerate(providers)}

        qs = (
            LivingOption.objects
            .select_related("provider")
            .prefetch_related("translations")
            .order_by("provider_id", "slug", "id")
        )

        data = []
        for lo in qs:
            item = {
                "provider_idx": provider_idx_by_id.get(lo.provider_id, 0),
                "slug": lo.slug or "",
                "care_level": lo.care_level,
                "cognitive_support_level": lo.cognitive_support_level,
                "wheelchair_accessible": bool(lo.wheelchair_accessible),
                "hearing_support": bool(lo.hearing_support),
                "visual_support": bool(lo.visual_support),
                "languages_supported": list(lo.languages_supported or []),
                "min_age": int(lo.min_age),
                "max_age": int(lo.max_age),
                "translations": {},
            }

            if include_provider_name:
                item["provider_name"] = lo.provider.name

            # Parler translations
            for tr in lo.translations.all():
                lang = tr.language_code
                item["translations"][lang] = {
                    "title": tr.title or "",
                    "description": tr.description or "",
                }

            data.append(item)

        if pretty_json:
            self.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
            return

        # Python literal (easy copy/paste into model_data.py)
        output_path = Path("model_data_dump.py")

        content_lines = []
        content_lines.append("MODEL_DATA = [")

        for item in data:
            formatted = pformat(item, width=100, sort_dicts=False)
            content_lines.append("    " + formatted.replace("\n", "\n    ") + ",")

        content_lines.append("]")

        output_path.write_text("\n".join(content_lines), encoding="utf-8")

        self.stdout.write(self.style.SUCCESS(f"Wrote {output_path} in readable format"))
