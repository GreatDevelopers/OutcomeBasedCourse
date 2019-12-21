import django_tables2 as tables
from .models import Institute


class InstituteTable(tables.Table):
    class Meta:
        model = Institute
        fields = ("institute_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no institute matching the search criteria..."
