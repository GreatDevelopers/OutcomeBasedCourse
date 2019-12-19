from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Institute, Level


class CreateInstituteForm(forms.Form):
    institute_name = forms.CharField(
        label="Institute Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter institute name",
            }
        ),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(CreateInstituteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateLevelForm(forms.Form):
    level_name = forms.CharField(
        label="Level Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter level name"}
        ),
        required=True,
    )
    institute = forms.ModelMultipleChoiceField(
        label="Institutes",
        queryset=Institute.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more than one.",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateLevelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateProgrammeForm(forms.Form):
    programme_code = forms.CharField(
        label="Programme Code",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter programme code",
            }
        ),
        required=True,
    )
    programme_name = forms.CharField(
        label="Programme Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter programme name",
            }
        ),
        required=True,
    )
    programme_fees = forms.IntegerField(
        label="Programme Fees",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter programme fees",
            }
        ),
    )
    level = forms.ModelChoiceField(
        label="Level",
        queryset=Level.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateProgrammeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))
