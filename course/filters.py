import django_filters
from .models import *


class CognitiveLevelFilter(django_filters.FilterSet):
    class Meta:
        model = CognitiveLevel
        fields = {"cognitive_level": ["icontains"]}


class ActionVerbFilter(django_filters.FilterSet):
    class Meta:
        model = ActionVerb
        fields = {
            "action_verb": ["icontains"],
            "cognitive_level__cognitive_level": ["icontains"],
        }


class OutcomeFilter(django_filters.FilterSet):
    class Meta:
        model = Outcome
        fields = {
            "outcome": ["icontains"],
            "action_verb__action_verb": ["icontains"],
        }


class ObjectiveFilter(django_filters.FilterSet):
    class Meta:
        model = Objective
        fields = {"objective": ["icontains"]}


class InstituteFilter(django_filters.FilterSet):
    class Meta:
        model = Institute
        fields = {"institute_name": ["icontains"]}


class LevelFilter(django_filters.FilterSet):
    institute_id = django_filters.ModelChoiceFilter(
        field_name="institute",
        lookup_expr="exact",
        empty_label="Select Institute",
        queryset=Institute.objects.all(),
    )

    class Meta:
        model = Level
        fields = {"level_name": ["icontains"]}


class ProgrammeFilter(django_filters.FilterSet):
    level_id = django_filters.ModelChoiceFilter(
        field_name="level",
        lookup_expr="exact",
        empty_label="Select Level",
        queryset=Level.objects.all(),
    )

    class Meta:
        model = Programme
        fields = {"programme_code": ["exact"], "programme_name": ["icontains"]}


class DisciplineFilter(django_filters.FilterSet):
    department_code = django_filters.ModelChoiceFilter(
        field_name="department",
        lookup_expr="exact",
        empty_label="Select Department",
        queryset=Department.objects.all(),
    )
    programme_code = django_filters.ModelChoiceFilter(
        field_name="programme",
        lookup_expr="exact",
        empty_label="Select Programme",
        queryset=Programme.objects.all(),
    )

    class Meta:
        model = Discipline
        fields = {
            "discipline_code": ["exact"],
            "discipline_name": ["icontains"],
        }


class CourseFilter(django_filters.FilterSet):
    discipline_code = django_filters.ModelChoiceFilter(
        field_name="discipline",
        lookup_expr="exact",
        empty_label="Select Discipline",
        queryset=Discipline.objects.all(),
    )

    class Meta:
        model = Course
        fields = {"course_id": ["exact"], "course_title": ["icontains"]}


class ModuleFilter(django_filters.FilterSet):
    course_id = django_filters.ModelChoiceFilter(
        field_name="course",
        lookup_expr="exact",
        empty_label="Select Course",
        queryset=Course.objects.all(),
    )

    class Meta:
        model = Module
        fields = {"module_title": ["icontains"]}


class UnitFilter(django_filters.FilterSet):
    module_id = django_filters.ModelChoiceFilter(
        field_name="module",
        lookup_expr="exact",
        empty_label="Select Module",
        queryset=Module.objects.all(),
    )

    class Meta:
        model = Unit
        fields = {"unit_name": ["icontains"]}
