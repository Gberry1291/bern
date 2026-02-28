from django.contrib import admin
from parler.admin import TranslatableAdmin
from core.models import LivingOption, Provider,LivingOptionEmbedding
from django.db.models import Count

@admin.register(LivingOption)
class LivingOptionAdmin(TranslatableAdmin):
    list_display = (
        "title",
        "provider",
        "care_level",
        "wheelchair_accessible",
        "embedding_exists",
    )
    readonly_fields = ()

    @admin.display(boolean=True, description="Embeddings generated?")
    def embedding_exists(self, obj):
        return LivingOptionEmbedding.objects.filter(
            living_option=obj,
            embedding__isnull=False
        ).exists()


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "verified",
        "self_registered",
        "updated_at",
        "living_options_count",
    )

    list_filter = ("status", "verified", "self_registered", "canton")
    search_fields = ("name", "contact_email", "contact_phone", "website_url")
    ordering = ("status", "-updated_at", "name")

    # Makes the edit page cleaner and review-friendly
    fieldsets = (
        ("Listing status", {
            "fields": ("status", "verified", "self_registered", "review_notes")
        }),
        ("Basic info", {
            "fields": ("name", "canton", "short_description")
        }),
        ("Support & accessibility", {
            "fields": (
                "support_level_low",
                "support_level_medium",
                "support_level_high",
                "wheelchair_accessible",
                "supported_languages",
            )
        }),
        ("Contact", {
            "fields": ("contact_email", "contact_phone", "website_url")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    actions = ("mark_pending", "publish_and_verify", "unverify_keep_published")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_living_options_count=Count("living_options"))

    @admin.display(ordering="_living_options_count", description="Living options")
    def living_options_count(self, obj):
        return obj._living_options_count

    @admin.action(description="Mark as pending review")
    def mark_pending(self, request, queryset):
        queryset.update(status="pending", verified=False)

    @admin.action(description="Publish + mark reviewed")
    def publish_and_verify(self, request, queryset):
        queryset.update(status="published", verified=True)

    @admin.action(description="Unverify (keep published)")
    def unverify_keep_published(self, request, queryset):
        queryset.update(verified=False)
