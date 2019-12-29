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


class InstituteView(SingleTableView):
    model = Institute
    template_name = "course/institute_list.html"
    context_object_name = "institute"
    ordering = ["institute_name"]

    def get_context_data(self, **kwargs):
        context = super(InstituteView, self).get_context_data(**kwargs)
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


class LevelView(ListView):
    model = Level
    template_name = "course/level_list.html"
    context_object_name = "level"
    ordering = ["level_name"]

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)
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


class ProgrammeView(ListView):
    model = Programme
    template_name = "course/programme_list.html"
    context_object_name = "programme"
    ordering = ["programme_name"]

    def get_context_data(self, **kwargs):
        context = super(ProgrammeView, self).get_context_data(**kwargs)
        table = ProgrammeTable(Programme.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["programme"] = table
        return context


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


class DisciplineView(ListView):
    model = Discipline
    template_name = "course/discipline_list.html"
    context_object_name = "discipline"
    ordering = ["discipline_name"]

    def get_context_data(self, **kwargs):
        context = super(DisciplineView, self).get_context_data(**kwargs)
        table = DisciplineTable(Discipline.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["discipline"] = table
        return context


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


class CourseView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "course"
    ordering = ["course_title"]

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        table = CourseTable(Course.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["course"] = table
        return context


class CourseFormView(FormView):
    template_name = "course/course_form.html"
    form_class = CourseForm
    success_url = reverse_lazy("course")

    def get_initial(self, **kwargs):
        self.edit_course = False
        if "course_id" in self.kwargs:
            course = Course.objects.filter(course_id=self.kwargs["course_id"])
            if course:
                self.edit_course = True
                initial_data = course.values()[0]
                initial_data["discipline"] = [
                    x for x in course.values_list("discipline", flat=True)
                ]
                initial_data["course_outcome"] = [
                    x for x in course.values_list("course_outcome", flat=True)
                ]
                initial_data["course_objective"] = [
                    x for x in course.values_list("course_objective", flat=True)
                ]
                return initial_data

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        discipline = cleaned_data.pop("discipline")
        outcome = cleaned_data.pop("course_outcome")
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
        course.course_outcome.set(outcome)
        course.course_objective.set(objective)
        return super().form_valid(form)


class ModuleView(ListView):
    model = Module
    template_name = "course/module_list.html"
    context_object_name = "module"
    ordering = ["module_title"]

    def get_context_data(self, **kwargs):
        context = super(ModuleView, self).get_context_data(**kwargs)
        table = ModuleTable(Module.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["module"] = table
        return context


class ModuleFormView(FormView):
    template_name = "course/module_form.html"
    form_class = ModuleForm
    success_url = reverse_lazy("module")

    def get_initial(self, **kwargs):
        self.edit_module = False
        if "module_id" in self.kwargs:
            module = Module.objects.filter(module_id=self.kwargs["module_id"])
            if module:
                self.edit_module = True
                initial_data = module.values()[0]
                initial_data["course"] = [
                    x for x in module.values_list("course", flat=True)
                ]
                initial_data["module_outcome"] = [
                    x for x in module.values_list("module_outcome", flat=True)
                ]
                initial_data["module_objective"] = [
                    x for x in module.values_list("module_objective", flat=True)
                ]
                return initial_data

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        course = cleaned_data.pop("course")
        outcome = cleaned_data.pop("module_outcome")
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
        module.module_outcome.set(outcome)
        module.module_objective.set(objective)
        return super().form_valid(form)


class UnitView(ListView):
    model = Unit
    template_name = "course/unit_list.html"
    context_object_name = "unit"
    ordering = ["unit_name"]

    def get_context_data(self, **kwargs):
        context = super(UnitView, self).get_context_data(**kwargs)
        table = UnitTable(Unit.objects.all())
        RequestConfig(self.request, paginate={"per_page": 30}).configure(table)
        context["unit"] = table
        return context


class UnitFormView(FormView):
    template_name = "course/unit_form.html"
    form_class = UnitForm
    success_url = reverse_lazy("unit")

    def get_initial(self, **kwargs):
        self.edit_unit = False
        if "unit_number" in self.kwargs:
            unit = Unit.objects.filter(unit_number=self.kwargs["unit_number"])
            if unit:
                self.edit_unit = True
                initial_data = unit.values()[0]
                initial_data["module"] = [
                    x for x in unit.values_list("module", flat=True)
                ]
                initial_data["unit_outcome"] = [
                    x for x in unit.values_list("unit_outcome", flat=True)
                ]
                initial_data["unit_objective"] = [
                    x for x in unit.values_list("unit_objective", flat=True)
                ]
                return initial_data

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        module = cleaned_data.pop("module")
        outcome = cleaned_data.pop("unit_outcome")
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
        unit.unit_outcome.set(outcome)
        unit.unit_objective.set(objective)
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
