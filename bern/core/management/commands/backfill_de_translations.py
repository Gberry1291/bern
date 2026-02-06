from django.core.management.base import BaseCommand
from parler.utils.context import switch_language
from core.models import LivingOption

class Command(BaseCommand):
    help = "Backfill German (de) translations for LivingOption if missing"

    def handle(self, *args, **kwargs):
        created = 0

        for lo in LivingOption.objects.all():
            if lo.has_translation("de"):
                continue

            # These attribute names assume your OLD fields were title/description
            # If you renamed them earlier, tell me and I’ll adjust
            old_title = getattr(lo, "title", None)
            old_desc = getattr(lo, "description", None)

            if not old_title and not old_desc:
                continue

            with switch_language(lo, "de"):
                lo.title = old_title or ""
                lo.description = old_desc or ""
                lo.save()

            created += 1

        self.stdout.write(self.style.SUCCESS(f"Created {created} German translations."))
