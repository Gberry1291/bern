from django import forms

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
