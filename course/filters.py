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
    class Meta:
        model = Level
        fields = {"level_name": ["icontains"]}


class ProgrammeFilter(django_filters.FilterSet):
    class Meta:
        model = Programme
        fields = {"programme_code": ["exact"], "programme_name": ["icontains"]}


class DisciplineFilter(django_filters.FilterSet):
    class Meta:
        model = Discipline
        fields = {
            "discipline_code": ["exact"],
            "discipline_name": ["icontains"],
            "department__department_name": ["icontains"],
        }


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {"course_id": ["exact"], "course_title": ["icontains"]}


class ModuleFilter(django_filters.FilterSet):
    class Meta:
        model = Module
        fields = {"module_title": ["icontains"]}


class UnitFilter(django_filters.FilterSet):
    class Meta:
        model = Unit
        fields = {"unit_name": ["icontains"]}
