from django import forms
from .models import Provider,LivingOption
from parler.forms import TranslatableModelForm
from django.utils.translation import gettext_lazy as _

LANGUAGE_CHOICES = [
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("it", "Italiano"),
    ("en", "English"),
]

class LivingOptionSearchForm(forms.Form):
    query = forms.CharField(label="Describe your needs", max_length=200)
    wheelchair_required = forms.BooleanField(required=False)
    min_care_level = forms.IntegerField(label="Minimum care level", required=False, min_value=0, max_value=5)
    languages = forms.MultipleChoiceField(
        label="Preferred languages",
        required=False,
        choices=LANGUAGE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

class ProviderRegistrationForm(forms.ModelForm):
    # Honeypot anti-spam (hidden in template)
    website = forms.CharField(required=False)

    class Meta:
        model = Provider
        fields = [
            "name",
            "canton",
            "short_description",
            "contact_email",
            "contact_phone",
            "website_url",
            "wheelchair_accessible",
            "support_level_low",
            "support_level_medium",
            "support_level_high",
        ]

    def clean_website(self):
        # If bots fill this hidden field, reject silently
        val = self.cleaned_data.get("website", "").strip()
        if val:
            raise forms.ValidationError("Spam detected")
        return val

class ProviderEditForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            "name", "canton", "short_description",
            "contact_email", "contact_phone", "website_url",
            "wheelchair_accessible",
            "support_level_low", "support_level_medium", "support_level_high",
            "supported_languages",
        ]

class LivingOptionCreateForm(TranslatableModelForm):
    # Three language-specific descriptions
    description_de = forms.CharField(
        required=False,
        label=_("Description (German)"),
        widget=forms.Textarea(attrs={"rows": 4}),
    )
    description_fr = forms.CharField(
        required=False,
        label=_("Description (French)"),
        widget=forms.Textarea(attrs={"rows": 4}),
    )
    description_it = forms.CharField(
        required=False,
        label=_("Description (Italian)"),
        widget=forms.Textarea(attrs={"rows": 4}),
    )
    description_en = forms.CharField(
        required=False,
        label=_("Description (English)"),
        widget=forms.Textarea(attrs={"rows": 4}),
    )

    class Meta:
        model = LivingOption
        fields = [
            "title",  # single title input; will be copied into each provided language
            "wheelchair_accessible",
            "hearing_support",
            "visual_support",
            "cognitive_support_level",
            "care_level",
            "min_age",
            "max_age",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": _("e.g. Supported studio apartment")}),
        }

    def clean(self):
        cleaned = super().clean()
        de = (cleaned.get("description_de") or "").strip()
        fr = (cleaned.get("description_fr") or "").strip()
        it = (cleaned.get("description_it") or "").strip()
        en = (cleaned.get("description_en") or "").strip()

        if not (de or fr or it or en):
            raise forms.ValidationError(_("Please provide a description in at least one language."))

        return cleaned

    def provided_languages(self):
        langs = []
        if (self.cleaned_data.get("description_de") or "").strip():
            langs.append("de")
        if (self.cleaned_data.get("description_fr") or "").strip():
            langs.append("fr")
        if (self.cleaned_data.get("description_it") or "").strip():
            langs.append("it")
        if (self.cleaned_data.get("description_en") or "").strip():
            langs.append("en")
        return langs

    def save(self, commit=True):
        obj = super().save(commit=False)

        langs = self.provided_languages()
        obj.languages_supported = langs

        if commit:
            obj.save()

            title = (self.cleaned_data.get("title") or "").strip()
            desc_map = {
                "de": (self.cleaned_data.get("description_de") or "").strip(),
                "fr": (self.cleaned_data.get("description_fr") or "").strip(),
                "it": (self.cleaned_data.get("description_it") or "").strip(),
                "en": (self.cleaned_data.get("description_en") or "").strip(),
            }

            # ✅ Write translations only for languages with content
            for lang in langs:
                obj.set_current_language(lang)
                obj.title = title
                obj.description = desc_map[lang]
                obj.save()

            # ✅ Delete translations for languages that are now empty
            for lang in ["de", "fr", "it", "en"]:
                if lang not in langs:
                    obj.translations.filter(language_code=lang).delete()

        return obj


class LivingOptionEditForm(LivingOptionCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        obj = kwargs.get("instance")
        if not obj:
            return

        # Prefill ONLY if that translation row exists (no fallback)
        for lang in ["de", "fr", "it", "en"]:
            desc = (
                obj.translations
                .filter(language_code=lang)
                .values_list("description", flat=True)
                .first()
            ) or ""
            self.fields[f"description_{lang}"].initial = desc
