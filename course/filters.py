import django_filters
from .models import Institute


class InstituteFilter(django_filters.FilterSet):
    class Meta:
        model = Institute
        fields = {"institute_name": ["icontains"]}
