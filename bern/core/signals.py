from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import LivingOption
from core.embeddings import generate_embedding
from django.conf import settings

# Track currently-processing instances to prevent recursion
_processing_instances = set()

# Fields that should trigger embedding regeneration if changed
FIELDS_TO_WATCH = [
    "title",
    "description",
    "cognitive_support_level",
    "care_level",
    "wheelchair_accessible",
    "hearing_support",
    "visual_support",
    "languages_supported",
]

@receiver(post_save, sender=LivingOption)
def generate_livingoption_embedding(sender, instance: LivingOption, **kwargs):
    """
    Generate/update embeddings only when relevant fields changed.
    Prevents recursion and unnecessary API calls.
    """
    if getattr(settings, "DISABLE_EMBEDDING_SIGNALS", False):
        return

    instance_id = instance.pk

    if instance_id in _processing_instances:
        return

    try:
        _processing_instances.add(instance_id)

        # Determine which fields triggered this save
        update_fields = kwargs.get("update_fields")

        # Only proceed if:
        # - update_fields is None (bulk save or creation)
        # - OR at least one watched field was updated
        if update_fields is not None:
            if not any(f in update_fields for f in FIELDS_TO_WATCH):
                return

        # Regenerate embedding
        text = instance.build_embedding_text()
        instance.embedding = generate_embedding(text)
        instance.save(update_fields=["embedding"])
        safe_title = instance.safe_translation_getter("title", any_language=True) or f"LivingOption {instance.pk}"
        print(f"Error generating embedding for {safe_title}: {e}")

    except Exception as e:
        safe_title = instance.safe_translation_getter("title", any_language=True) or f"LivingOption {instance.pk}"
        print(f"Error generating embedding for {safe_title}: {e}")
    finally:
        _processing_instances.discard(instance_id)
