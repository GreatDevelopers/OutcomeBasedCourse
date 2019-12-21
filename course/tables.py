import django_tables2 as tables
from .models import *


class InstituteTable(tables.Table):
    class Meta:
        model = Institute
        fields = ("institute_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no institute matching the search criteria..."


class LevelTable(tables.Table):
    class Meta:
        model = Level
        fields = ("level_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no level matching the search criteria..."


class ProgrammeTable(tables.Table):
    class Meta:
        model = Programme
        fields = ("programme_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no programme matching the search criteria..."


class DisciplineTable(tables.Table):
    class Meta:
        model = Discipline
        fields = ("discipline_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no discipline matching the search criteria..."


class CourseTable(tables.Table):
    class Meta:
        model = Course
        fields = ("course_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no course matching the search criteria..."


class ModuleTable(tables.Table):
    class Meta:
        model = Module
        fields = ("module_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no module matching the search criteria..."


class UnitTable(tables.Table):
    class Meta:
        model = Unit
        fields = ("unit_name",)
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There is no unit matching the search criteria..."
