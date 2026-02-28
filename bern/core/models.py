from django.db import models
from django.contrib.auth.models import User
from pgvector.django import VectorField,HnswIndex
from parler.models import TranslatableModel, TranslatedFields
from parler.admin import TranslatableAdmin
import hashlib
import secrets
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError


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
    # Core identity
    name = models.CharField(max_length=255)
    canton = models.CharField(max_length=50)

    STATUS_CHOICES = [
        ("published", "Published"),
        ("pending", "Pending review"),
        ("rejected", "Rejected"),
    ]

    status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
        default="published",   # safe default for your existing sample data
    )

    review_notes = models.TextField(
        blank=True,
        default="",
        help_text="Internal notes (not shown publicly)"
    )

    # Listing status
    verified = models.BooleanField(
        default=False,
        help_text="Reviewed for completeness and clarity"
    )

    # Descriptive content
    short_description = models.TextField(
        blank=True,
        default="",
        help_text="Plain-language description of the provider"
    )

    # What they offer
    support_level_low = models.BooleanField(default=False)
    support_level_medium = models.BooleanField(default=False)
    support_level_high = models.BooleanField(default=False)

    wheelchair_accessible = models.BooleanField(
        default=False,
        help_text="Step-free access and wheelchair-usable spaces"
    )

    supported_languages = models.JSONField(
        default=list,
        help_text="ISO language codes, e.g. ['de', 'fr', 'it']"
    )

    # Contact info (displayed, not used to message yet)
    contact_email = models.EmailField(
        blank=True,
        default=""
    )

    contact_phone = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    website_url = models.URLField(
        blank=True,
        default=""
    )

    # Meta
    self_registered = models.BooleanField(
        default=True,
        help_text="True if provider submitted their own listing"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=120)
    slug = models.SlugField(max_length=255, default="", db_index=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["provider", "slug"], name="uniq_provider_slug"),
        ]

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


    def clean(self):
        if self.min_age > self.max_age:
            raise ValidationError("min_age must be <= max_age")

    def build_embedding_text(self) -> str:
        title = self.safe_translation_getter("title", any_language=True) or ""
        desc  = self.safe_translation_getter("description", any_language=True) or ""

        keywords = []
        if self.wheelchair_accessible:
            keywords += ["wheelchair accessible", "rollstuhlgängig", "accessible aux fauteuils roulants", "accessibile in sedia a rotelle"]
        if self.cognitive_support_level:
            keywords += ["cognitive support", "kognitive Unterstützung", "soutien cognitif", "supporto cognitivo"]

        return (
            f"Title: {title}\n"
            f"Title (repeat): {title}\n"
            f"Description: {desc}\n"
            f"Care level: {self.care_level}\n"
            f"Cognitive support level: {self.get_cognitive_support_level_display()}\n"
            f"Wheelchair accessible: {self.wheelchair_accessible}\n"
            f"Hearing support: {self.hearing_support}\n"
            f"Visual support: {self.visual_support}\n"
            f"Languages supported: {', '.join(self.languages_supported or [])}\n"
            f"Age range: {self.min_age}-{self.max_age}\n"
            f"Keywords: {', '.join(keywords)}\n"
        )

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
            f"Age range: {self.min_age}-{self.max_age}\n"
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
        indexes = [
            HnswIndex(
                name="loe_embedding_hnsw",
                fields=["embedding"],
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            ),
        ]

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


class ProviderMagicLink(models.Model):
    PURPOSE_CHOICES = [
        ("edit", "Edit listing"),
    ]

    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_name="magic_links")
    email = models.EmailField(default="", blank=True)

    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default="edit")

    token_hash = models.CharField(max_length=64, db_index=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    # Expire links automatically
    expires_at = models.DateTimeField(default=timezone.now)
    used_at = models.DateTimeField(null=True, blank=True, default=None)

    @staticmethod
    def mint_raw_token() -> str:
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_token(raw: str) -> str:
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    @classmethod
    def create_link(cls, provider, email: str, ttl_minutes: int = 60):
        raw = cls.mint_raw_token()
        obj = cls.objects.create(
            provider=provider,
            email=email or "",
            token_hash=cls.hash_token(raw),
            expires_at=timezone.now() + timedelta(minutes=ttl_minutes),
        )
        return raw, obj

    def is_valid(self) -> bool:
        if self.used_at is not None:
            return False
        return timezone.now() <= self.expires_at
