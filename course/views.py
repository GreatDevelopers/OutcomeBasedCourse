from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django_tables2 import RequestConfig, SingleTableView
from .models import *
from .forms import (
    CreateInstituteForm,
    CreateLevelForm,
    CreateProgrammeForm,
    CreateDisciplineForm,
    CreateCourseForm,
    CreateModuleForm,
    CreateUnitForm,
)
from .tables import InstituteTable


class InstituteView(SingleTableView):
    model = Institute
    template_name = "course/institute_list.html"
    context_object_name = "institute"
    ordering = ["institute_name"]

    def get_context_data(self, **kwargs):
        context = super(InstituteView, self).get_context_data(**kwargs)
        table = InstituteTable(Institute.objects.values('institute_name'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CreateInstituteView(FormView):
    template_name = "course/institute_form.html"
    form_class = CreateInstituteForm
    success_url = reverse_lazy("institute")

    def form_valid(self, form):
        Institute.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class LevelView(ListView):
    model = Level
    template_name = "course/level_list.html"


class CreateLevelView(FormView):
    template_name = "course/create_level_form.html"
    form_class = CreateLevelForm
    success_url = reverse_lazy("level")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        institute = cleaned_data.pop("institute")
        level = Level.objects.create(**cleaned_data)
        level.save()
        level.institute.set(institute)
        return super().form_valid(form)


class ProgrammeView(ListView):
    model = Programme
    template_name = "course/programme_list.html"


class CreateProgrammeView(FormView):
    template_name = "course/create_programme_form.html"
    form_class = CreateProgrammeForm
    success_url = reverse_lazy("programme")

    def form_valid(self, form):
        Programme.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class DisciplineView(ListView):
    model = Discipline
    template_name = "course/discipline_list.html"


class CreateDisciplineView(FormView):
    template_name = "course/create_discipline_form.html"
    form_class = CreateDisciplineForm
    success_url = reverse_lazy("discipline")

    def form_valid(self, form):
        Discipline.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)


class CourseView(ListView):
    model = Course
    template_name = "course/course_list.html"


class CreateCourseView(FormView):
    template_name = "course/create_course_form.html"
    form_class = CreateCourseForm
    success_url = reverse_lazy("course")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        discipline = cleaned_data.pop("discipline")
        course = Course.objects.create(**cleaned_data)
        course.save()
        course.discipline.set(discipline)
        return super().form_valid(form)


class ModuleView(ListView):
    model = Module
    template_name = "course/module_list.html"


class CreateModuleView(FormView):
    template_name = "course/create_module_form.html"
    form_class = CreateModuleForm
    success_url = reverse_lazy("module")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        course = cleaned_data.pop("course")
        module = Module.objects.create(**cleaned_data)
        module.save()
        module.course.set(course)
        return super().form_valid(form)


class UnitView(ListView):
    model = Unit
    template_name = "course/unit_list.html"


class CreateUnitView(FormView):
    template_name = "course/create_unit_form.html"
    form_class = CreateUnitForm
    success_url = reverse_lazy("unit")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        module = cleaned_data.pop("module")
        unit = Unit.objects.create(**cleaned_data)
        unit.save()
        unit.module.set(module)
        return super().form_valid(form)
