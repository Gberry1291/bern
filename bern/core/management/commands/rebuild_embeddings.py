import os
from django.core.management.base import BaseCommand
from openai import OpenAI

from django.db import transaction
from core.models import LivingOption, LivingOptionEmbedding  # adjust if needed

SUPPORTED = ["de", "fr", "it", "en"]
EMBEDDING_MODEL = "text-embedding-3-small"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def embed_text(text: str):
    try:
        resp = client.embeddings.create(model=EMBEDDING_MODEL, input=text)
        return resp.data[0].embedding, None
    except Exception as e:
        return None, str(e)

class Command(BaseCommand):
    help = "Rebuild LivingOption embeddings per language (strict: only embed if translation exists)"

    def add_arguments(self, parser):
        parser.add_argument("--lang", type=str, default="de", help="Language code (de/fr/it/en)")
        parser.add_argument("--all", action="store_true", help="Build embeddings for all languages")
        parser.add_argument("--only-missing", action="store_true", help="Only create missing embeddings")
        parser.add_argument("--limit", type=int, default=0, help="Limit number of options (0 = no limit)")

    @transaction.atomic
    def handle(self, *args, **opts):
        langs = SUPPORTED if opts["all"] else [opts["lang"]]
        langs = [l for l in langs if l in SUPPORTED]

        only_missing = opts["only_missing"]
        limit = opts["limit"]

        qs = LivingOption.objects.all().prefetch_related("translations").order_by("id")
        if limit:
            qs = qs[:limit]

        total = 0
        for lo in qs:
            for lang in langs:
                if only_missing and LivingOptionEmbedding.objects.filter(living_option=lo, language=lang).exists():
                    continue

                # ✅ Strict: only embed if description exists in that language (no fallback)
                desc = (
                    lo.translations
                      .filter(language_code=lang)
                      .values_list("description", flat=True)
                      .first()
                ) or ""
                if not desc.strip():
                    continue

                # Use your existing helper if you want, but ONLY if it doesn't fall back.
                # We'll build a minimal text here to avoid any fallback issues:
                title = (
                    lo.translations
                      .filter(language_code=lang)
                      .values_list("title", flat=True)
                      .first()
                ) or ""

                text = (
                    f"Title: {title}\n"
                    f"Description: {desc}\n"
                    f"Care level: {lo.care_level}\n"
                    f"Cognitive support: {lo.cognitive_support_level}\n"
                    f"Wheelchair accessible: {lo.wheelchair_accessible}\n"
                    f"Hearing support: {lo.hearing_support}\n"
                    f"Visual support: {lo.visual_support}\n"
                )

                emb, err = embed_text(text)
                if emb is None:
                    self.stdout.write(self.style.WARNING(f"Embedding failed for lo#{lo.id} lang={lang}: {err}"))
                    continue

                LivingOptionEmbedding.objects.update_or_create(
                    living_option=lo,
                    language=lang,
                    defaults={"embedding": emb},
                )
                total += 1

        self.stdout.write(self.style.SUCCESS(f"Updated/created {total} embeddings."))
