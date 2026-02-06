from django.contrib import admin
from parler.admin import TranslatableAdmin
from core.models import LivingOption, Provider

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

    def embedding_exists(self, obj):
        return obj.embedding is not None
    embedding_exists.boolean = True  # shows as a green checkmark
    embedding_exists.short_description = "Embedding generated?"

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "verified", "living_options_count")

    def living_options_count(self, obj):
        return obj.livingoption_set.count()
