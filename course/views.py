from .forms import CreateInstituteForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Institute


class InstituteView(ListView):
    model = Institute
    template_name = "course/institute_list.html"


class CreateInstituteView(FormView):
    template_name = "course/institute_form.html"
    form_class = CreateInstituteForm
    success_url = "/"

    def form_valid(self, form):
        Institute.objects.create(**form.cleaned_data).save()
        return super().form_valid(form)
