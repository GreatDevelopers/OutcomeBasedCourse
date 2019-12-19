from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Institute, Level, Programme, Discipline, Course
from .forms import (
    CreateInstituteForm,
    CreateLevelForm,
    CreateProgrammeForm,
    CreateDisciplineForm,
    CreateCourseForm,
)


class InstituteView(ListView):
    model = Institute
    template_name = "course/institute_list.html"


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
        discipline = cleaned_data.pop("course_discipline")
        course = Course.objects.create(**cleaned_data)
        course.save()
        course.course_discipline.set(discipline)
        return super().form_valid(form)
