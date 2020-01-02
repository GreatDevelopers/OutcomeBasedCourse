from django.urls import reverse
from django.utils.safestring import mark_safe
import django_tables2 as tables
import bootstrap4.templatetags.bootstrap4 as bootstrap
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
    edit = tables.Column(
        verbose_name="Edit Outcome",
        accessor=tables.A("id"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Outcome
        fields = ("outcome", "outcome_short_name", "action_verb")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no outcome matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_edit(self, value):
        url = reverse("edit-outcome", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class ObjectiveTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Objective",
        accessor=tables.A("id"),
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Objective
        fields = ("objective", "objective_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no objective matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_edit(self, value):
        url = reverse("edit-objective", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))


class InstituteTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Institute",
        accessor=tables.A("institute_id"),
        attrs={"td": {"align": "center"}},
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Institute
        fields = ("institute_name", "institute_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no institute matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_institute_name(self, value):
        institute_id = Institute.objects.get(institute_name=value).institute_id
        url = (reverse("level") + "?institute_id=%s") % (institute_id,)
        return mark_safe(
            bootstrap.bootstrap_button(
                content=value,
                href=url,
                button_class="btn-link",
                extra_classes="text-body",
            )
        )

    def render_edit(self, value):
        url = reverse("edit-institute", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class LevelTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Level",
        accessor=tables.A("level_id"),
        attrs={"td": {"align": "center"}},
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Level
        fields = ("level_name", "level_short_name", "institute")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no level matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_level_name(self, value):
        level_id = Level.objects.get(level_name=value).level_id
        url = (reverse("programme") + "?level_id=%s") % (level_id,)
        return mark_safe(
            bootstrap.bootstrap_button(
                content=value,
                href=url,
                button_class="btn-link",
                extra_classes="text-body",
            )
        )

    def render_edit(self, value):
        url = reverse("edit-level", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class ProgrammeTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Programme",
        accessor=tables.A("programme_code"),
        attrs={"td": {"align": "center"}},
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
            "level",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no programme matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_programme_name(self, value):
        programme_code = Programme.objects.get(
            programme_name=value
        ).programme_code
        url = (reverse("discipline") + "?programme_code=%s") % (programme_code,)
        return mark_safe(
            bootstrap.bootstrap_button(
                content=value,
                href=url,
                button_class="btn-link",
                extra_classes="text-body",
            )
        )

    def render_edit(self, value):
        url = reverse("edit-programme", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class DepartmentTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Department",
        accessor=tables.A("department_code"),
        attrs={"td": {"align": "center"}},
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Department
        fields = ("department_code", "department_name", "department_short_name")
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no department matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_edit(self, value):
        url = reverse("edit-department", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class DisciplineTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Discipline",
        accessor=tables.A("discipline_code"),
        attrs={"td": {"align": "center"}},
        orderable=False,
        exclude_from_export=True,
    )

    class Meta:
        model = Discipline
        fields = (
            "discipline_code",
            "discipline_name",
            "discipline_short_name",
            "total_credits",
            "department",
            "programme",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no discipline matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_discipline_name(self, value):
        discipline_code = Discipline.objects.get(
            discipline_name=value
        ).discipline_code
        url = (reverse("course") + "?discipline_code=%s") % (discipline_code,)
        return mark_safe(
            bootstrap.bootstrap_button(
                content=value,
                href=url,
                button_class="btn-link",
                extra_classes="text-body",
            )
        )

    def render_edit(self, value):
        url = reverse("edit-discipline", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class CourseTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Course",
        accessor=tables.A("course_id"),
        attrs={"td": {"align": "center"}},
        orderable=False,
        exclude_from_export=True,
    )

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
            "discipline",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no course matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_course_title(self, value):
        course_id = Course.objects.get(course_title=value).course_id
        url = (reverse("module") + "?course_id=%s") % (course_id,)
        return mark_safe(
            bootstrap.bootstrap_button(
                content=value,
                href=url,
                button_class="btn-link",
                extra_classes="text-body",
            )
        )

    def render_edit(self, value):
        url = reverse("edit-course", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class ModuleTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Module",
        accessor=tables.A("module_id"),
        orderable=False,
        exclude_from_export=True,
    )

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
            "course",
        )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no module matching the search criteria..."

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_edit(self, value):
        url = reverse("edit-module", args=[value])
        return mark_safe(
            bootstrap.bootstrap_button(
                content="Edit", href=url, button_class="btn-link"
            )
        )


class UnitTable(tables.Table):
    edit = tables.Column(
        verbose_name="Edit Unit",
        accessor=tables.A("unit_number"),
        orderable=False,
        exclude_from_export=True,
    )

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

    def before_render(self, request):
        if self.request.user.is_authenticated == False:
            self.columns.hide("edit")

    def render_edit(self, value):
        url = reverse("edit-unit", args=[value])
        return mark_safe('<a href="%s">Edit</a>' % (url,))
