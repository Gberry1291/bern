from django.db import models
from django.contrib.auth.models import User
from pgvector.django import VectorField
from parler.models import TranslatableModel, TranslatedFields
from parler.admin import TranslatableAdmin


class SearchEvent(models.Model):
    query = models.TextField()
    lang = models.CharField(max_length=5, default="de")
    wheelchair_required = models.BooleanField(null=True, blank=True)
    care_target = models.IntegerField(null=True, blank=True)
    language_filter = models.CharField(max_length=10, null=True, blank=True)

    query_embedding = VectorField(dimensions=1536, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SearchEvent #{self.pk} [{self.lang}] {self.query[:40]}"


class SearchClick(models.Model):
    event = models.ForeignKey(SearchEvent, on_delete=models.CASCADE, related_name="clicks")
    living_option = models.ForeignKey("LivingOption", on_delete=models.CASCADE)
    rank_shown = models.IntegerField()  # 0-based position in results
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Click event={self.event_id} option={self.living_option_id} rank={self.rank_shown}"


class Provider(models.Model):
    name = models.CharField(max_length=255)
    canton = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    supported_languages = models.JSONField(
        default=list,
        help_text="ISO language codes, e.g. ['de', 'fr', 'it']"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProviderMembership(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("editor", "Editor"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ("user", "provider")

    def __str__(self):
        return f"{self.user.username} → {self.provider.name} ({self.role})"


class LivingOption(TranslatableModel):

    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(),
    )

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="living_options"
    )

    # ---- Structured filters ----
    wheelchair_accessible = models.BooleanField(default=False)
    hearing_support = models.BooleanField(default=False)
    visual_support = models.BooleanField(default=False)

    cognitive_support_level = models.IntegerField(
        choices=[
            (0, "None"),
            (1, "Mild"),
            (2, "Moderate"),
            (3, "Severe"),
        ]
    )

    care_level = models.IntegerField(
        help_text="1 = minimal, 5 = 24/7 care"
    )

    languages_supported = models.JSONField(default=list)

    # ---- Vector embedding ----
    embedding = VectorField(
        dimensions=1536,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or f"LivingOption {self.pk}"

    def build_embedding_text(self) -> str:
        keywords = []
        if self.wheelchair_accessible:
            keywords += ["wheelchair accessible", "rollstuhlgängig", "accessible aux fauteuils roulants", "accessibile in sedia a rotelle"]
        if self.cognitive_support_level:
            keywords += ["cognitive support", "kognitive Unterstützung", "soutien cognitif", "supporto cognitivo"]
        return f"""
    Title: {self.title}
    Description:{self.description}
    Care level: {self.care_level}
    Cognitive support level: {self.get_cognitive_support_level_display()}
    Wheelchair accessible: {self.wheelchair_accessible}
    Hearing support: {self.hearing_support}
    Visual support: {self.visual_support}
    Languages supported: {", ".join(self.languages_supported)}
    """

    def get_localized_text(self, lang: str) -> str:
        """
        Build the text we embed/search against in a specific language.
        Falls back to German if that translation doesn't exist.
        """
        title = self.safe_translation_getter("title", language_code=lang, any_language=True) or ""
        desc = self.safe_translation_getter("description", language_code=lang, any_language=True) or ""

        return (
            f"Title: {title}\n"
            f"Description: {desc}\n"
            f"Care level: {self.care_level}\n"
            f"Cognitive support: {self.cognitive_support_level}\n"
            f"Wheelchair accessible: {self.wheelchair_accessible}\n"
            f"Hearing support: {self.hearing_support}\n"
            f"Visual support: {self.visual_support}\n"
            f"Languages supported: {', '.join(self.languages_supported)}\n"
        )

class LivingOptionEmbedding(models.Model):
    LANG_CHOICES = [("de","de"), ("fr","fr"), ("it","it"), ("en","en")]

    living_option = models.ForeignKey(
        "LivingOption",
        on_delete=models.CASCADE,
        related_name="embeddings",
    )
    language = models.CharField(max_length=5, choices=LANG_CHOICES)
    embedding = VectorField(dimensions=1536)  # adjust if your embedding model differs
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("living_option", "language")

    def __str__(self):
        return f"Embedding {self.living_option_id} [{self.language}]"

class SearchImpression(models.Model):
    event = models.ForeignKey(SearchEvent, on_delete=models.CASCADE, related_name="impressions")
    living_option = models.ForeignKey("LivingOption", on_delete=models.CASCADE)

    rank_shown = models.IntegerField()  # global 0-based rank in displayed results
    clicked = models.BooleanField(default=False)
    skipped = models.BooleanField(default=False)  # marked when user clicks something below
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event", "living_option")

    def __str__(self):
        return f"Impression event={self.event_id} option={self.living_option_id} rank={self.rank_shown}"
