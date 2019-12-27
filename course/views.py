from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from django_tables2 import RequestConfig, SingleTableView
from .models import *
from .forms import *
from .tables import *
from OutcomeBasedCourse.config.verbose_names import *


def home_page(request):
    return render(request, "course/home_page.html")


class CognitiveLevelView(SingleTableView):
    model = CognitiveLevel
    template_name = "course/cognitive_level_list.html"
    context_object_name = "cognitive_level"
    ordering = ["cognitive_level"]

    def get_context_data(self, **kwargs):
        context = super(CognitiveLevelView, self).get_context_data(**kwargs)
        table = CognitiveLevelTable(CognitiveLevel.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["cognitive_level"] = table
        return context


class CreateCognitiveLevelView(FormView):
    template_name = "course/create_cognitive_level_form.html"
    form_class = CreateCognitiveLevelForm
    success_url = reverse_lazy("cognitive-level")

    def form_valid(self, form):
        CognitiveLevel.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class ActionVerbView(SingleTableView):
    model = ActionVerb
    template_name = "course/action_verb_list.html"
    context_object_name = "action_verb"
    ordering = ["action_verb"]

    def get_context_data(self, **kwargs):
        context = super(ActionVerbView, self).get_context_data(**kwargs)
        table = ActionVerbTable(ActionVerb.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["action_verb"] = table
        return context


class CreateActionVerbView(FormView):
    template_name = "course/create_action_verb_form.html"
    form_class = CreateActionVerbForm
    success_url = reverse_lazy("action-verb")

    def form_valid(self, form):
        ActionVerb.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class OutcomeView(SingleTableView):
    model = Outcome
    template_name = "course/outcome_list.html"
    context_object_name = "outcome"
    ordering = ["outcome"]

    def get_context_data(self, **kwargs):
        context = super(OutcomeView, self).get_context_data(**kwargs)
        table = OutcomeTable(Outcome.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["outcome"] = table
        return context


class CreateOutcomeView(FormView):
    template_name = "course/create_outcome_form.html"
    form_class = CreateOutcomeForm
    success_url = reverse_lazy("outcome")

    def form_valid(self, form):
        Outcome.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class ObjectiveView(SingleTableView):
    model = Objective
    template_name = "course/objective_list.html"
    context_object_name = "objective"
    ordering = ["objective"]

    def get_context_data(self, **kwargs):
        context = super(ObjectiveView, self).get_context_data(**kwargs)
        table = ObjectiveTable(Objective.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["objective"] = table
        return context


class CreateObjectiveView(FormView):
    template_name = "course/create_objective_form.html"
    form_class = CreateObjectiveForm
    success_url = reverse_lazy("objective")

    def form_valid(self, form):
        Objective.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class InstituteView(SingleTableView):
    model = Institute
    template_name = "course/institute_list.html"
    context_object_name = "institute"
    ordering = ["institute_name"]

    def get_context_data(self, **kwargs):
        context = super(InstituteView, self).get_context_data(**kwargs)
        context["INSTITUTE"] = INSTITUTE_PLURAL
        table = InstituteTable(Institute.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["institute"] = table
        return context


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

    def get_context_data(self, **kwargs):
        context = super(InstituteFormView, self).get_context_data(**kwargs)
        context["INSTITUTE"] = INSTITUTE_SINGULAR
        return context


class LevelView(ListView):
    model = Level
    template_name = "course/level_list.html"
    context_object_name = "level"
    ordering = ["level_name"]

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)
        context["LEVEL"] = LEVEL_PLURAL
        table = LevelTable(Level.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["level"] = table
        return context


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

    def get_context_data(self, **kwargs):
        context = super(LevelFormView, self).get_context_data(**kwargs)
        context["LEVEL"] = LEVEL_SINGULAR
        return context


class ProgrammeView(ListView):
    model = Programme
    template_name = "course/programme_list.html"
    context_object_name = "programme"
    ordering = ["programme_name"]

    def get_context_data(self, **kwargs):
        context = super(ProgrammeView, self).get_context_data(**kwargs)
        context["PROGRAMME"] = PROGRAMME_PLURAL
        table = ProgrammeTable(Programme.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["programme"] = table
        return context


class CreateProgrammeView(FormView):
    template_name = "course/create_programme_form.html"
    form_class = CreateProgrammeForm
    success_url = reverse_lazy("programme")

    def form_valid(self, form):
        Programme.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateProgrammeView, self).get_context_data(**kwargs)
        context["PROGRAMME"] = PROGRAMME_SINGULAR
        return context


class DepartmentView(ListView):
    model = Department
    template_name = "course/department_list.html"
    context_object_name = "department"
    ordering = ["department_name"]

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        context["DEPARTMENT"] = DEPARTMENT_PLURAL
        table = DepartmentTable(Department.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["department"] = table
        return context


class CreateDepartmentView(FormView):
    template_name = "course/create_department_form.html"
    form_class = CreateDepartmentForm
    success_url = reverse_lazy("department")

    def form_valid(self, form):
        Department.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateDepartmentView, self).get_context_data(**kwargs)
        context["DEPARTMENT"] = DEPARTMENT_SINGULAR
        return context


class DisciplineView(ListView):
    model = Discipline
    template_name = "course/discipline_list.html"
    context_object_name = "discipline"
    ordering = ["discipline_name"]

    def get_context_data(self, **kwargs):
        context = super(DisciplineView, self).get_context_data(**kwargs)
        context["DISCIPLINE"] = DISCIPLINE_PLURAL
        table = DisciplineTable(Discipline.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["discipline"] = table
        return context


class CreateDisciplineView(FormView):
    template_name = "course/create_discipline_form.html"
    form_class = CreateDisciplineForm
    success_url = reverse_lazy("discipline")

    def form_valid(self, form):
        Discipline.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateDisciplineView, self).get_context_data(**kwargs)
        context["DISCIPLINE"] = DISCIPLINE_SINGULAR
        return context


class CourseView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "course"
    ordering = ["course_title"]

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context["COURSE"] = COURSE_PLURAL
        table = CourseTable(Course.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["course"] = table
        return context


class CreateCourseView(FormView):
    template_name = "course/create_course_form.html"
    form_class = CreateCourseForm
    success_url = reverse_lazy("course")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        discipline = cleaned_data.pop("discipline")
        outcome = cleaned_data.pop("course_outcome")
        objective = cleaned_data.pop("course_objective")
        course = Course.objects.create(**cleaned_data)
        course.save()
        course.discipline.set(discipline)
        course.course_outcome.set(outcome)
        course.course_objective.set(objective)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateCourseView, self).get_context_data(**kwargs)
        context["COURSE"] = COURSE_SINGULAR
        return context


class ModuleView(ListView):
    model = Module
    template_name = "course/module_list.html"
    context_object_name = "module"
    ordering = ["module_title"]

    def get_context_data(self, **kwargs):
        context = super(ModuleView, self).get_context_data(**kwargs)
        context["MODULE"] = MODULE_PLURAL
        table = ModuleTable(Module.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["module"] = table
        return context


class CreateModuleView(FormView):
    template_name = "course/create_module_form.html"
    form_class = CreateModuleForm
    success_url = reverse_lazy("module")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        course = cleaned_data.pop("course")
        outcome = cleaned_data.pop("module_outcome")
        objective = cleaned_data.pop("module_objective")
        module = Module.objects.create(**cleaned_data)
        module.save()
        module.course.set(course)
        module.module_outcome.set(outcome)
        module.module_objective.set(objective)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateModuleView, self).get_context_data(**kwargs)
        context["MODULE"] = MODULE_SINGULAR
        return context


class UnitView(ListView):
    model = Unit
    template_name = "course/unit_list.html"
    context_object_name = "unit"
    ordering = ["unit_name"]

    def get_context_data(self, **kwargs):
        context = super(UnitView, self).get_context_data(**kwargs)
        context["UNIT"] = UNIT_PLURAL
        table = UnitTable(Unit.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["unit"] = table
        return context


class CreateUnitView(FormView):
    template_name = "course/create_unit_form.html"
    form_class = CreateUnitForm
    success_url = reverse_lazy("unit")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        module = cleaned_data.pop("module")
        outcome = cleaned_data.pop("unit_outcome")
        objective = cleaned_data.pop("unit_objective")
        unit = Unit.objects.create(**cleaned_data)
        unit.save()
        unit.module.set(module)
        unit.unit_outcome.set(outcome)
        unit.unit_objective.set(objective)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateUnitView, self).get_context_data(**kwargs)
        context["UNIT"] = UNIT_SINGULAR
        return context


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
        for module in modules:
            units = Unit.objects.filter(module=module)
            context["units"] = units.values(
                "unit_name",
                "unit_overview",
                "unit_outcome",
                "unit_objective",
                "unit_body",
                "unit_resources",
                "unit_test",
                "module",
            )
        return context
