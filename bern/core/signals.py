from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import translation
from django.conf import settings
from django.apps import apps

from core.models import LivingOption, LivingOptionEmbedding
from core.embeddings import generate_embedding

_processing_instances = set()

TranslationModel = apps.get_model(
    LivingOption._meta.app_label,
    f"{LivingOption.__name__}Translation"
)

@receiver(post_save, sender=TranslationModel)
def regenerate_embedding_on_translation_save(sender, instance, **kwargs):
    lo = instance.master
    lang = instance.language_code

    text = build_embedding_text_for_lang(lo, lang)
    if not text:
        LivingOptionEmbedding.objects.filter(living_option=lo, language=lang).delete()
        return

    emb = generate_embedding(text)
    LivingOptionEmbedding.objects.update_or_create(
        living_option=lo,
        language=lang,
        defaults={"embedding": emb},
    )

FIELDS_TO_WATCH = [
    "cognitive_support_level",
    "care_level",
    "wheelchair_accessible",
    "hearing_support",
    "visual_support",
    "languages_supported",
    # NOTE: title/description changes often happen in Parler translation table,
    # so LivingOption.post_save may NOT catch them reliably.
]

SUPPORTED = ["de", "fr", "it", "en"]

def build_embedding_text_for_lang(lo: LivingOption, lang: str) -> str:
    title = lo.safe_translation_getter("title", language_code=lang, any_language=False) or ""
    desc  = lo.safe_translation_getter("description", language_code=lang, any_language=False) or ""
    if not (title.strip() or desc.strip()):
        return ""

    return f"""
Title: {title}
Title (repeat): {title}

Description:
{desc}

Care level: {lo.care_level}
Cognitive support level: {lo.cognitive_support_level}

Wheelchair accessible: {lo.wheelchair_accessible}
Hearing support: {lo.hearing_support}
Visual support: {lo.visual_support}
Languages supported: {", ".join(lo.languages_supported or [])}
""".strip()

@receiver(post_save, sender=LivingOption)
def generate_livingoption_embeddings(sender, instance: LivingOption, **kwargs):
    if getattr(settings, "DISABLE_EMBEDDING_SIGNALS", False):
        return

    instance_id = instance.pk
    if instance_id in _processing_instances:
        return

    try:
        _processing_instances.add(instance_id)

        update_fields = kwargs.get("update_fields")
        if update_fields is not None:
            if not any(f in update_fields for f in FIELDS_TO_WATCH):
                # Still regenerate if we don't know (or on create) — but you can keep it strict
                pass

        # Update per-language embedding rows used by search
        for lang in SUPPORTED:
            translation.activate(lang)
            text = build_embedding_text_for_lang(instance, lang)

            if not text:
                LivingOptionEmbedding.objects.filter(living_option=instance, language=lang).delete()
                continue

            emb = generate_embedding(text)
            LivingOptionEmbedding.objects.update_or_create(
                living_option=instance,
                language=lang,
                defaults={"embedding": emb},
            )

    except Exception as e:
        safe_title = instance.safe_translation_getter("title", any_language=True) or f"LivingOption {instance.pk}"
        print(f"Error generating embedding for {safe_title}: {e}")
    finally:
        _processing_instances.discard(instance_id)
