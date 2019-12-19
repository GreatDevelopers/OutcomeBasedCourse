from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Institute, Level
from .forms import CreateInstituteForm, CreateLevelForm


class InstituteView(ListView):
    model = Institute
    template_name = "course/institute_list.html"


class CreateInstituteView(FormView):
    template_name = "course/institute_form.html"
    form_class = CreateInstituteForm
    success_url = reverse_lazy("institute")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        if cleaned_data["level"].exists():
            for level in form.cleaned_data["level"]:
                cleaned_data["level"] = level
                Institute.objects.create(**cleaned_data).save()
        else:
            cleaned_data["level"] = None
            Institute.objects.create(**cleaned_data).save()
        return super().form_valid(form)


class LevelView(ListView):
    model = Institute
    template_name = "course/level_list.html"


class CreateLevelView(FormView):
    template_name = "course/create_level_form.html"
    form_class = CreateLevelForm
    success_url = reverse_lazy("level")

    def form_valid(self, form):
        Level.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)
