from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import (
    CognitiveLevel,
    ActionVerb,
    Outcome,
    Objective,
    Institute,
    Level,
    Programme,
    Department,
    Discipline,
    Course,
    Module,
)
from martor.fields import MartorFormField
from OutcomeBasedCourse.config.verbose_names import *

# from djmoney.forms import MoneyWidget


class CreateCognitiveLevelForm(forms.Form):
    cognitive_level = forms.CharField(
        label="Cognitive level",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter cognitive level",
            }
        ),
        required=True,
    )
    cognitive_level_short_name = forms.CharField(
        label="Cognitive level short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateCognitiveLevelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateActionVerbForm(forms.Form):
    action_verb = forms.CharField(
        label="Action verb",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter action verb"}
        ),
        required=True,
    )
    action_verb_short_name = forms.CharField(
        label="Action verb short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    cognitive_level = forms.ModelChoiceField(
        label="Cognitive Level",
        queryset=CognitiveLevel.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(CreateActionVerbForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateOutcomeForm(forms.Form):
    outcome = forms.CharField(
        label="Outcome",
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter outcome"}
        ),
        required=True,
    )
    outcome_short_name = forms.CharField(
        label="Outcome short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    action_verb = forms.ModelChoiceField(
        label="Action Verb",
        queryset=ActionVerb.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(CreateOutcomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateObjectiveForm(forms.Form):
    objective = forms.CharField(
        label="Objective",
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter objective"}
        ),
        required=True,
    )
    objective_short_name = forms.CharField(
        label="Objective short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateObjectiveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateInstituteForm(forms.Form):
    institute_name = forms.CharField(
        label=INSTITUTE_SINGULAR + " Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter institute name",
            }
        ),
        required=True,
    )
    institute_short_name = forms.CharField(
        label=INSTITUTE_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateInstituteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateLevelForm(forms.Form):
    level_name = forms.CharField(
        label=LEVEL_SINGULAR + " Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter level name"}
        ),
        required=True,
    )
    level_short_name = forms.CharField(
        label=LEVEL_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    institute = forms.ModelMultipleChoiceField(
        label=INSTITUTE_PLURAL,
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
        label=PROGRAMME_SINGULAR + " Code",
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
        label=PROGRAMME_SINGULAR + " Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter programme name",
            }
        ),
        required=True,
    )
    programme_short_name = forms.CharField(
        label=PROGRAMME_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    programme_fees = forms.IntegerField(
        label=PROGRAMME_SINGULAR + " Fees",
        # Will be used for money field
        # widget=MoneyWidget(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter programme fees",
            }
        ),
        required=False,
    )
    level = forms.ModelChoiceField(
        label=LEVEL_SINGULAR,
        queryset=Level.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateProgrammeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateDepartmentForm(forms.Form):
    department_code = forms.CharField(
        label=DEPARTMENT_SINGULAR + " Code",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter department code",
            }
        ),
        required=True,
    )
    department_name = forms.CharField(
        label=DEPARTMENT_SINGULAR + " Name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter department name",
            }
        ),
        required=True,
    )
    department_short_name = forms.CharField(
        label=DEPARTMENT_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateDepartmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateDisciplineForm(forms.Form):
    discipline_code = forms.CharField(
        label=DISCIPLINE_SINGULAR + " Code",
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
        label=DISCIPLINE_SINGULAR + " Name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter discipline name",
            }
        ),
        required=True,
    )
    discipline_short_name = forms.CharField(
        label=DISCIPLINE_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
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
        required=False,
    )
    programme = forms.ModelChoiceField(
        label=PROGRAMME_SINGULAR,
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
        label=COURSE_SINGULAR + " id",
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
    course_short_name = forms.CharField(
        label=COURSE_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    course_overview = MartorFormField(
        label="Overview",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course overview",
            }
        ),
        required=False,
    )
    course_outcome = forms.ModelMultipleChoiceField(
        label="Outcome",
        queryset=Outcome.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )
    course_objective = forms.ModelMultipleChoiceField(
        label="Objective",
        queryset=Objective.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
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
    lecture_contact_hours_per_week = forms.DecimalField(
        label="Lecture contact hours per week",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter lecture contact hours",
            }
        ),
        required=True,
    )
    tutorial_contact_hours_per_week = forms.DecimalField(
        label="Tutorial contact hours per week",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter tutorial contact hours",
            }
        ),
        required=True,
    )
    practical_contact_hours_per_week = forms.DecimalField(
        label="Practical contact hours per week",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter practical contact hours",
            }
        ),
        required=True,
    )
    course_resources = MartorFormField(
        label="Resources",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter course resources",
            }
        ),
        required=False,
    )
    course_test = MartorFormField(
        label="Test",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter course test"}
        ),
        required=False,
    )
    discipline = forms.ModelMultipleChoiceField(
        label=DISCIPLINE_PLURAL,
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
    module_short_name = forms.CharField(
        label=MODULE_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    module_overview = MartorFormField(
        label="Overview",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module overview",
            }
        ),
        required=False,
    )
    module_outcome = forms.ModelMultipleChoiceField(
        label="Outcome",
        queryset=Outcome.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )
    module_objective = forms.ModelMultipleChoiceField(
        label="Objective",
        queryset=Objective.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )
    module_body = MartorFormField(
        label="Body",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter module body"}
        ),
        required=False,
    )
    module_resources = MartorFormField(
        label="Resources",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter module resources",
            }
        ),
        required=False,
    )
    module_test = MartorFormField(
        label="Test",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter module test"}
        ),
        required=False,
    )
    course = forms.ModelMultipleChoiceField(
        label=COURSE_PLURAL,
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


class CreateUnitForm(forms.Form):
    unit_name = forms.CharField(
        label="Name",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter unit name"}
        ),
        required=False,
    )
    unit_short_name = forms.CharField(
        label=UNIT_SINGULAR + " short name",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter short name"}
        ),
        required=False,
    )
    unit_overview = MartorFormField(
        label="Overview",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter unit overview",
            }
        ),
        required=False,
    )
    unit_outcome = forms.ModelMultipleChoiceField(
        label="Outcome",
        queryset=Outcome.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )
    unit_objective = forms.ModelMultipleChoiceField(
        label="Objective",
        queryset=Objective.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )
    unit_body = MartorFormField(
        label="Body",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter unit body"}
        ),
        required=False,
    )
    unit_resources = MartorFormField(
        label="Resources",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter unit resources",
            }
        ),
        required=False,
    )
    unit_test = MartorFormField(
        label="Test",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter unit test"}
        ),
        required=False,
    )
    module = forms.ModelMultipleChoiceField(
        label=MODULE_PLURAL,
        queryset=Module.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        help_text="Hold down “Control”, or “Command” on a Mac, to select more "
        "than one.",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateUnitForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))
