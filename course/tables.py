from django.urls import reverse
from django.utils.safestring import mark_safe
import django_tables2 as tables
from .models import *


class CognitiveLevelTable(tables.Table):
    class Meta:
        model = CognitiveLevel
        fields = ("cognitive_level", "cognitive_level_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = (
            "There is no cognitive level matching the search criteria..."
        )


class ActionVerbTable(tables.Table):
    class Meta:
        model = ActionVerb
        fields = ("action_verb", "action_verb_short_name", "cognitive_level")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no action verb matching the search criteria..."


class OutcomeTable(tables.Table):
    class Meta:
        model = Outcome
        fields = ("outcome", "outcome_short_name", "action_verb")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no outcome matching the search criteria..."


class ObjectiveTable(tables.Table):
    class Meta:
        model = Objective
        fields = ("objective", "objective_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no objective matching the search criteria..."


class InstituteTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Institute",
        accessor=tables.A("institute_id"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Institute
        fields = ("institute_name", "institute_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no institute matching the search criteria..."

    def render_edit(self, value):
        url = reverse("edit-institute", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class LevelTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Level",
        accessor=tables.A("level_id"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Level
        fields = ("level_name", "level_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no level matching the search criteria..."

    def render_edit(self, value):
        url = reverse("edit-level", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class ProgrammeTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Programme",
        accessor=tables.A("programme_code"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Programme
        fields = (
            "programme_code",
            "programme_name",
            "programme_short_name",
            "programme_fees",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no programme matching the search criteria..."

    def render_edit(self, value):
        url = reverse("edit-programme", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class DepartmentTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Department",
        accessor=tables.A("department_code"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Department
        fields = ("department_code", "department_name", "department_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no department matching the search criteria..."

    def render_edit(self, value):
        url = reverse("edit-department", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class DisciplineTable(tables.Table):
    class Meta:
        model = Discipline
        fields = (
            "discipline_code",
            "discipline_name",
            "discipline_short_name",
            "total_credits",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no discipline matching the search criteria..."


class CourseTable(tables.Table):
    class Meta:
        model = Course
        fields = (
            "course_id",
            "course_title",
            "course_short_name",
            "course_overview",
            "course_outcome",
            "course_objective",
            "course_credit",
            "lecture_contact_hours_per_week",
            "tutorial_contact_hours_per_week",
            "practical_contact_hours_per_week",
            "course_resources",
            "course_test",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no course matching the search criteria..."


class ModuleTable(tables.Table):
    class Meta:
        model = Module
        fields = (
            "module_title",
            "module_short_name",
            "module_overview",
            "module_outcome",
            "module_objective",
            "module_body",
            "module_resources",
            "module_test",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no module matching the search criteria..."


class UnitTable(tables.Table):
    class Meta:
        model = Unit
        fields = (
            "unit_name",
            "unit_short_name",
            "unit_overview",
            "unit_outcome",
            "unit_objective",
            "unit_body",
            "unit_resources",
            "unit_test",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no unit matching the search criteria..."
