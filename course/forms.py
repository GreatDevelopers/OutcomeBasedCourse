from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Institute, Level, Programme, Discipline, Course


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
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
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


class CreateDisciplineForm(forms.Form):
    discipline_code = forms.CharField(
        label="Discipline Code",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter discipline code",
            }
        ),
        required=True,
    )
    discipline_name = forms.CharField(
        label="Discipline Name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter discipline name",
            }
        ),
        required=True,
    )
    total_credits = forms.DecimalField(
        label="Total Credits",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter total credits",
            }
        ),
    )
    programme = forms.ModelChoiceField(
        label="Programme",
        queryset=Programme.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateDisciplineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateCourseForm(forms.Form):
    course_id = forms.CharField(
        label="Course id",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter course id"}
        ),
        required=True,
    )
    course_title = forms.CharField(
        label="Title",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter course title"}
        ),
        required=True,
    )
    course_overview = forms.CharField(
        label="Overview",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course overview",
            }
        ),
        required=False,
    )
    course_outcome = forms.CharField(
        label="Outcome",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course outcomes",
            }
        ),
        required=False,
    )
    course_objective = forms.CharField(
        label="Objective",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course objective",
            }
        ),
        required=False,
    )
    course_credit = forms.DecimalField(
        label="Credit",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course credits",
            }
        ),
        required=True,
    )
    contact_hours_per_week = forms.DecimalField(
        label="Contact hours per week",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter total credits",
            }
        ),
        required=True,
    )
    course_resources = forms.CharField(
        label="Resources",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course resources",
            }
        ),
        required=False,
    )
    course_test = forms.CharField(
        label="Test",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter course test"}
        ),
        required=False,
    )
    discipline = forms.ModelMultipleChoiceField(
        label="Discipline",
        queryset=Discipline.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateModuleForm(forms.Form):
    module_title = forms.CharField(
        label="Title",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter module title"}
        ),
        required=True,
    )
    module_overview = forms.CharField(
        label="Overview",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module overview",
            }
        ),
        required=False,
    )
    module_outcome = forms.CharField(
        label="Outcome",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module outcomes",
            }
        ),
        required=False,
    )
    module_objective = forms.CharField(
        label="Objective",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module objective",
            }
        ),
        required=False,
    )
    module_resources = forms.CharField(
        label="Resources",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module resources",
            }
        ),
        required=False,
    )
    module_test = forms.CharField(
        label="Test",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter module test"}
        ),
        required=False,
    )
    course = forms.ModelMultipleChoiceField(
        label="Course",
        queryset=Course.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateModuleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))
