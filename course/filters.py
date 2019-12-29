import django_filters
from .models import *


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
