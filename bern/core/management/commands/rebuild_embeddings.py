from django.core.management.base import BaseCommand
from django.utils import translation
from core.models import LivingOption, LivingOptionEmbedding
from core.embeddings import generate_embedding  # your existing function

SUPPORTED = ["de", "fr", "it", "en"]

class Command(BaseCommand):
    help = "Rebuild LivingOption embeddings per language"

    def add_arguments(self, parser):
        parser.add_argument("--lang", type=str, default="de", help="Language code (de/fr/it/en)")
        parser.add_argument("--all", action="store_true", help="Build embeddings for all languages")
        parser.add_argument("--only-missing", action="store_true", help="Only create missing embeddings")
        parser.add_argument("--limit", type=int, default=0, help="Limit number of options (0 = no limit)")

    def handle(self, *args, **opts):
        langs = SUPPORTED if opts["all"] else [opts["lang"]]
        only_missing = opts["only_missing"]
        limit = opts["limit"]

        qs = LivingOption.objects.all().order_by("id")
        if limit:
            qs = qs[:limit]

        total = 0
        for lo in qs:
            for lang in langs:
                # Optionally skip if translation doesn't exist in that language:
                # If you want strict behavior, uncomment this check:
                # if not lo.has_translation(lang):
                #     continue

                if only_missing and LivingOptionEmbedding.objects.filter(living_option=lo, language=lang).exists():
                    continue

                # Activate language (helps Parler pick correct translation)
                translation.activate(lang)

                text = lo.get_localized_text(lang).strip()
                if not text:
                    continue

                emb = generate_embedding(text)
                if emb is None:
                    continue

                obj, _ = LivingOptionEmbedding.objects.update_or_create(
                    living_option=lo,
                    language=lang,
                    defaults={"embedding": emb},
                )
                total += 1

        self.stdout.write(self.style.SUCCESS(f"Updated/created {total} embeddings."))
