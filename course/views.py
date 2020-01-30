from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.shortcuts import render
from django_tables2 import RequestConfig, SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from .models import *
from .forms import *
from .tables import *
from .filters import *
from OutcomeBasedCourse.config.verbose_names import *

from django.views import View
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML as weasy_html


def home_page(request):
    return render(request, "course/home_page.html")


class CognitiveLevelView(SingleTableMixin, FilterView):
    model = CognitiveLevel
    table_class = CognitiveLevelTable
    filterset_class = CognitiveLevelFilter
    context_table_name = "cognitive_level_table"
    pagination = {"per_page": 30}
    ordering = ["cognitive_level"]
    template_name = "course/cognitive_level_list.html"


class CreateCognitiveLevelView(FormView):
    template_name = "course/create_cognitive_level_form.html"
    form_class = CreateCognitiveLevelForm
    success_url = reverse_lazy("cognitive-level")

    def form_valid(self, form):
        CognitiveLevel.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class ActionVerbView(SingleTableMixin, FilterView):
    model = ActionVerb
    table_class = ActionVerbTable
    filterset_class = ActionVerbFilter
    context_table_name = "action_verb_table"
    pagination = {"per_page": 30}
    ordering = ["action_verb"]
    template_name = "course/action_verb_list.html"


class CreateActionVerbView(FormView):
    template_name = "course/create_action_verb_form.html"
    form_class = CreateActionVerbForm
    success_url = reverse_lazy("action-verb")

    def form_valid(self, form):
        ActionVerb.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class OutcomeView(SingleTableMixin, FilterView):
    model = Outcome
    table_class = OutcomeTable
    filterset_class = OutcomeFilter
    context_table_name = "outcome_table"
    pagination = {"per_page": 30}
    ordering = ["outcome"]
    template_name = "course/outcome_list.html"


class OutcomeFormView(FormView):
    template_name = "course/outcome_form.html"
    form_class = OutcomeForm
    success_url = reverse_lazy("outcome")

    def get_initial(self, **kwargs):
        self.edit_outcome = False
        if "outcome_id" in self.kwargs:
            outcome = Outcome.objects.filter(id=self.kwargs["outcome_id"])
            if outcome:
                self.edit_outcome = True
                initial_data = outcome.values()[0]
                initial_data["action_verb"] = initial_data.pop("action_verb_id")
                return initial_data

    def form_valid(self, form):
        if self.edit_outcome:
            Outcome.objects.filter(id=self.kwargs["outcome_id"]).update(
                **form.cleaned_data
            )
        else:
            Outcome.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class ObjectiveView(SingleTableMixin, FilterView):
    model = Objective
    table_class = ObjectiveTable
    filterset_class = ObjectiveFilter
    context_table_name = "objective_table"
    pagination = {"per_page": 30}
    ordering = ["objective"]
    template_name = "course/objective_list.html"


class ObjectiveFormView(FormView):
    template_name = "course/objective_form.html"
    form_class = ObjectiveForm
    success_url = reverse_lazy("objective")

    def get_initial(self, **kwargs):
        self.edit_objective = False
        if "objective_id" in self.kwargs:
            objective = Objective.objects.filter(id=self.kwargs["objective_id"])
            if objective:
                self.edit_objective = True
                initial_data = objective.values()[0]
                return initial_data

    def form_valid(self, form):
        if self.edit_objective:
            Objective.objects.filter(id=self.kwargs["objective_id"]).update(
                **form.cleaned_data
            )
        else:
            Objective.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class InstituteView(SingleTableMixin, FilterView):
    model = Institute
    table_class = InstituteTable
    filterset_class = InstituteFilter
    context_table_name = "institute_table"
    pagination = {"per_page": 30}
    ordering = ["institute_name"]
    template_name = "course/institute_list.html"


class InstituteFormView(FormView):
    template_name = "course/institute_form.html"
    form_class = InstituteForm
    success_url = reverse_lazy("institute")

    def get_initial(self, **kwargs):
        self.edit_institute = False
        if "institute_id" in self.kwargs:
            institute = Institute.objects.filter(
                institute_id=self.kwargs["institute_id"]
            )
            if institute:
                self.edit_institute = True
                return institute.values()[0]

    def form_valid(self, form):
        if self.edit_institute:
            Institute.objects.filter(
                institute_id=self.kwargs["institute_id"]
            ).update(**form.cleaned_data)
        else:
            Institute.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class LevelView(SingleTableMixin, FilterView):
    model = Level
    table_class = LevelTable
    filterset_class = LevelFilter
    context_table_name = "level_table"
    pagination = {"per_page": 30}
    ordering = ["level_name"]
    template_name = "course/level_list.html"


class LevelFormView(FormView):
    template_name = "course/level_form.html"
    form_class = LevelForm
    success_url = reverse_lazy("level")

    def get_initial(self, **kwargs):
        self.edit_level = False
        if "level_id" in self.kwargs:
            level = Level.objects.filter(level_id=self.kwargs["level_id"])
            if level:
                self.edit_level = True
                initial_data = level.values()[0]
                initial_data["institute"] = [
                    x for x in level.values_list("institute", flat=True)
                ]
                return initial_data

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        institute = cleaned_data.pop("institute")
        if self.edit_level:
            Level.objects.filter(level_id=self.kwargs["level_id"]).update(
                **cleaned_data
            )
            level = Level.objects.get(level_id=self.kwargs["level_id"])
        else:
            level = Level.objects.create(**cleaned_data)
            level.save()
        level.institute.set(institute)
        return super().form_valid(form)


class ProgrammeView(SingleTableMixin, FilterView):
    model = Programme
    table_class = ProgrammeTable
    filterset_class = ProgrammeFilter
    context_table_name = "programme_table"
    pagination = {"per_page": 30}
    ordering = ["programme_name"]
    template_name = "course/programme_list.html"


class ProgrammeFormView(FormView):
    template_name = "course/programme_form.html"
    form_class = ProgrammeForm
    success_url = reverse_lazy("programme")

    def get_initial(self, **kwargs):
        self.edit_programme = False
        if "programme_code" in self.kwargs:
            programme = Programme.objects.filter(
                programme_code=self.kwargs["programme_code"]
            )
            if programme:
                self.edit_programme = True
                initial_data = programme.values()[0]
                initial_data["level"] = initial_data.pop("level_id")
                return initial_data

    def form_valid(self, form):
        if self.edit_programme:
            Programme.objects.filter(
                programme_code=self.kwargs["programme_code"]
            ).update(**form.cleaned_data)
        else:
            Programme.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class DepartmentView(ListView):
    model = Department
    template_name = "course/department_list.html"
    context_object_name = "department"
    ordering = ["department_name"]

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        table = DepartmentTable(Department.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["department"] = table
        return context


class DepartmentFormView(FormView):
    template_name = "course/department_form.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("department")

    def get_initial(self, **kwargs):
        self.edit_department = False
        if "department_code" in self.kwargs:
            department = Department.objects.filter(
                department_code=self.kwargs["department_code"]
            )
            if department:
                self.edit_department = True
                initial_data = department.values()[0]
                return initial_data

    def form_valid(self, form):
        if self.edit_department:
            Department.objects.filter(
                department_code=self.kwargs["department_code"]
            ).update(**form.cleaned_data)
        else:
            Department.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class DisciplineView(SingleTableMixin, FilterView):
    model = Discipline
    table_class = DisciplineTable
    filterset_class = DisciplineFilter
    context_table_name = "discipline_table"
    pagination = {"per_page": 30}
    ordering = ["discipline_name"]
    template_name = "course/discipline_list.html"


class DisciplineFormView(FormView):
    template_name = "course/discipline_form.html"
    form_class = DisciplineForm
    success_url = reverse_lazy("discipline")

    def get_initial(self, **kwargs):
        self.edit_discipline = False
        if "discipline_code" in self.kwargs:
            discipline = Discipline.objects.filter(
                discipline_code=self.kwargs["discipline_code"]
            )
            if discipline:
                self.edit_discipline = True
                initial_data = discipline.values()[0]
                initial_data["programme"] = initial_data.pop("programme_id")
                return initial_data

    def form_valid(self, form):
        if self.edit_discipline:
            Discipline.objects.filter(
                discipline_code=self.kwargs["discipline_code"]
            ).update(**form.cleaned_data)
        else:
            Discipline.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class CourseView(SingleTableMixin, FilterView):
    model = Course
    table_class = CourseTable
    filterset_class = CourseFilter
    context_table_name = "course_table"
    pagination = {"per_page": 30}
    ordering = ["course_title"]
    template_name = "course/course_list.html"


class CourseFormView(FormView):
    template_name = "course/course_form.html"
    form_class = CourseForm
    success_url = reverse_lazy("course")

    def get_context_data(self, **kwargs):
        context = super(CourseFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["outcomes"] = OutcomeFormSet(self.request.POST)
        elif self.edit_course:
            context["outcomes"] = OutcomeFormSet(
                queryset=self.course.course_outcome.all()
            )
        else:
            context["outcomes"] = OutcomeFormSet(
                queryset=Outcome.objects.none()
            )

        return context

    def get_initial(self, **kwargs):
        self.edit_course = False
        if "course_id" in self.kwargs:
            try:
                course = Course.objects.get(course_id=self.kwargs["course_id"])
            except Course.DoesNotExist:
                pass
            else:
                self.edit_course = True
                self.course = course
                initial_data = Course.objects.filter(
                    course_id=self.kwargs["course_id"]
                ).values()[0]
                initial_data["discipline"] = self.course.discipline.all()
                initial_data[
                    "course_objective"
                ] = self.course.course_objective.all()
                return initial_data

    def form_valid(self, form, **kwargs):
        super(CourseFormView, self).get_context_data(**kwargs)
        context = self.get_context_data()
        outcomes_formset = context["outcomes"]
        if not outcomes_formset.is_valid():
            return super().form_invalid(form)

        cleaned_data = form.cleaned_data
        discipline = cleaned_data.pop("discipline")
        cleaned_data.pop("course_outcome")
        objective = cleaned_data.pop("course_objective")
        if self.edit_course:
            Course.objects.filter(course_id=self.kwargs["course_id"]).update(
                **cleaned_data
            )
            course = Course.objects.get(course_id=self.kwargs["course_id"])
        else:
            course = Course.objects.create(**cleaned_data)
            course.save()
        course.discipline.set(discipline)
        course.course_objective.set(objective)

        outcome_list = []
        for outcome_form in outcomes_formset:

            # Check if outcome is to be deassociated from course
            # Then don't add it to outcome_list
            if outcome_form in outcomes_formset.deleted_forms:
                continue

            outcome = outcome_form.instance
            try:
                outcome = Outcome.objects.get(
                    outcome=outcome.outcome,
                    outcome_short_name=outcome.outcome_short_name,
                    action_verb=outcome.action_verb,
                )
                outcome_list.append(outcome)
            # This exception occurs when outcome form is empty thus action_verb
            # is also empty
            except Outcome.action_verb.RelatedObjectDoesNotExist:
                continue
            # Create outcome if it doesn't already exists in database
            except Outcome.DoesNotExist:
                outcome = outcome_form.save()
                outcome_list.append(outcome)

        course.course_outcome.set(outcome_list)

        return super().form_valid(form)


class ModuleView(SingleTableMixin, FilterView):
    model = Module
    table_class = ModuleTable
    filterset_class = ModuleFilter
    context_table_name = "module_table"
    pagination = {"per_page": 30}
    ordering = ["module_title"]
    template_name = "course/module_list.html"


class ModuleFormView(FormView):
    template_name = "course/module_form.html"
    form_class = ModuleForm
    success_url = reverse_lazy("module")

    def get_context_data(self, **kwargs):
        context = super(ModuleFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["outcomes"] = OutcomeFormSet(self.request.POST)
        elif self.edit_module:
            context["outcomes"] = OutcomeFormSet(
                queryset=self.module.module_outcome.all()
            )
        else:
            context["outcomes"] = OutcomeFormSet(
                queryset=Outcome.objects.none()
            )

        return context

    def get_initial(self, **kwargs):
        self.edit_module = False
        if "module_id" in self.kwargs:
            try:
                module = Module.objects.get(module_id=self.kwargs["module_id"])
            except Module.DoesNotExist:
                pass
            else:
                self.edit_module = True
                self.module = module
                initial_data = Module.objects.filter(
                    module_id=self.kwargs["module_id"]
                ).values()[0]
                initial_data["course"] = self.module.course.all()
                initial_data[
                    "module_objective"
                ] = self.module.module_objective.all()
                return initial_data

    def form_valid(self, form, **kwargs):
        super(ModuleFormView, self).get_context_data(**kwargs)
        context = self.get_context_data()
        outcomes_formset = context["outcomes"]
        if not outcomes_formset.is_valid():
            return super().form_invalid(form)

        cleaned_data = form.cleaned_data
        course = cleaned_data.pop("course")
        cleaned_data.pop("module_outcome")
        objective = cleaned_data.pop("module_objective")
        if self.edit_module:
            Module.objects.filter(module_id=self.kwargs["module_id"]).update(
                **cleaned_data
            )
            module = Module.objects.get(module_id=self.kwargs["module_id"])
        else:
            module = Module.objects.create(**cleaned_data)
            module.save()
        module.course.set(course)
        module.module_objective.set(objective)

        outcome_list = []
        for outcome_form in outcomes_formset:

            # Check if outcome is to be deassociated from module
            # Then don't add it to outcome_list
            if outcome_form in outcomes_formset.deleted_forms:
                continue

            outcome = outcome_form.instance
            try:
                outcome = Outcome.objects.get(
                    outcome=outcome.outcome,
                    outcome_short_name=outcome.outcome_short_name,
                    action_verb=outcome.action_verb,
                )
                outcome_list.append(outcome)
            # This exception occurs when outcome form is empty thus action_verb
            # is also empty
            except Outcome.action_verb.RelatedObjectDoesNotExist:
                continue
            # Create outcome if it doesn't already exists in database
            except Outcome.DoesNotExist:
                outcome = outcome_form.save()
                outcome_list.append(outcome)

        module.module_outcome.set(outcome_list)

        return super().form_valid(form)


class UnitView(SingleTableMixin, FilterView):
    model = Unit
    table_class = UnitTable
    filterset_class = UnitFilter
    context_table_name = "unit_table"
    pagination = {"per_page": 30}
    ordering = ["unit_name"]
    template_name = "course/unit_list.html"


class UnitFormView(FormView):
    template_name = "course/unit_form.html"
    form_class = UnitForm
    success_url = reverse_lazy("unit")

    def get_context_data(self, **kwargs):
        context = super(UnitFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["outcomes"] = OutcomeFormSet(self.request.POST)
        elif self.edit_unit:
            context["outcomes"] = OutcomeFormSet(
                queryset=self.unit.unit_outcome.all()
            )
        else:
            context["outcomes"] = OutcomeFormSet(
                queryset=Outcome.objects.none()
            )

        return context

    def get_initial(self, **kwargs):
        self.edit_unit = False
        if "unit_number" in self.kwargs:
            try:
                unit = Unit.objects.get(unit_number=self.kwargs["unit_number"])
            except Unit.DoesNotExist:
                pass
            else:
                self.edit_unit = True
                self.unit = unit
                initial_data = Unit.objects.filter(
                    unit_number=self.kwargs["unit_number"]
                ).values()[0]
                initial_data["module"] = self.unit.module.all()
                initial_data["unit_objective"] = self.unit.unit_objective.all()
                return initial_data

    def form_valid(self, form, **kwargs):
        super(UnitFormView, self).get_context_data(**kwargs)
        context = self.get_context_data()
        outcomes_formset = context["outcomes"]
        if not outcomes_formset.is_valid():
            return super().form_invalid(form)

        cleaned_data = form.cleaned_data
        module = cleaned_data.pop("module")
        cleaned_data.pop("unit_outcome")
        objective = cleaned_data.pop("unit_objective")
        if self.edit_unit:
            Unit.objects.filter(unit_number=self.kwargs["unit_number"]).update(
                **cleaned_data
            )
            unit = Unit.objects.get(unit_number=self.kwargs["unit_number"])
        else:
            unit = Unit.objects.create(**cleaned_data)
            unit.save()
        unit.module.set(module)
        unit.unit_objective.set(objective)

        outcome_list = []
        for outcome_form in outcomes_formset:

            # Check if outcome is to be deassociated from unit
            # Then don't add it to outcome_list
            if outcome_form in outcomes_formset.deleted_forms:
                continue

            outcome = outcome_form.instance
            try:
                outcome = Outcome.objects.get(
                    outcome=outcome.outcome,
                    outcome_short_name=outcome.outcome_short_name,
                    action_verb=outcome.action_verb,
                )
                outcome_list.append(outcome)
            # This exception occurs when outcome form is empty thus action_verb
            # is also empty
            except Outcome.action_verb.RelatedObjectDoesNotExist:
                continue
            # Create outcome if it doesn't already exists in database
            except Outcome.DoesNotExist:
                outcome = outcome_form.save()
                outcome_list.append(outcome)

        unit.unit_outcome.set(outcome_list)

        return super().form_valid(form)


class SyllabusView(TemplateView):
    template_name = "course/view_syllabus.html"
    context_object_name = "syllabus"

    def get_context_data(self, **kwargs):
        context = super(SyllabusView, self).get_context_data(**kwargs)
        course = Course.objects.get(course_id=self.kwargs["course_id"])
        context["course_name"] = course.course_title
        context["course_overview"] = course.course_overview
        context["course_credit"] = course.course_credit
        context[
            "lecture_contact_hours_per_week"
        ] = course.lecture_contact_hours_per_week
        context[
            "tutorial_contact_hours_per_week"
        ] = course.tutorial_contact_hours_per_week
        context[
            "practical_contact_hours_per_week"
        ] = course.practical_contact_hours_per_week
        context["course_objective"] = course.course_objective
        context["course_outcome"] = course.course_outcome
        context["course_test"] = course.course_test
        context["course_resources"] = course.course_resources
        context["course_id"] = course.course_id
        modules = Module.objects.filter(course=course)
        context["modules"] = modules.values(
            "module_title",
            "module_overview",
            "module_outcome",
            "module_objective",
            "module_body",
            "module_resources",
            "module_test",
        )
        units = []
        attributes = []
        for module in modules:
            units.append(Unit.objects.filter(module=module))
        for unit in units:
            attributes.append(
                unit.values(
                    "unit_name",
                    "unit_overview",
                    "unit_outcome",
                    "unit_objective",
                    "unit_body",
                    "unit_resources",
                    "unit_test",
                    "module",
                )
            )
        context["units"] = attributes
        return context


class html_to_pdf(View):
    context_object_name = "syllabus"

    def get_context_data(self, **kwargs):
        context = {}
        course = Course.objects.get(course_id=self.kwargs["course_id"])
        context["course_name"] = course.course_title
        context["course_overview"] = course.course_overview
        context["course_credit"] = course.course_credit
        context[
            "lecture_contact_hours_per_week"
        ] = course.lecture_contact_hours_per_week
        context[
            "tutorial_contact_hours_per_week"
        ] = course.tutorial_contact_hours_per_week
        context[
            "practical_contact_hours_per_week"
        ] = course.practical_contact_hours_per_week
        context["course_objective"] = course.course_objective
        context["course_outcome"] = course.course_outcome
        context["course_test"] = course.course_test
        context["course_resources"] = course.course_resources
        modules = Module.objects.filter(course=course)
        context["modules"] = modules.values(
            "module_title",
            "module_overview",
            "module_outcome",
            "module_objective",
            "module_body",
            "module_resources",
            "module_test",
            "module_id",
        )
        units = []
        attributes = []
        for module in modules:
            units.append(Unit.objects.filter(module=module))
        for unit in units:
            attributes.append(
                unit.values(
                    "unit_name",
                    "unit_overview",
                    "unit_outcome",
                    "unit_objective",
                    "unit_body",
                    "unit_resources",
                    "unit_test",
                    "module",
                )
            )
        context["units"] = attributes
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        html_string = render_to_string("course/render_syllabus.html", context)

        html = weasy_html(string=html_string)
        html.write_pdf(target="/tmp/mypdf.pdf")

        fs = FileSystemStorage("/tmp")
        with fs.open("mypdf.pdf") as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="mypdf.pdf"'
            return response

        # return response
