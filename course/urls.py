from django.urls import path
from .views import (
    InstituteView,
    CreateInstituteView,
    LevelView,
    CreateLevelView,
    ProgrammeView,
    CreateProgrammeView,
    DisciplineView,
    CreateDisciplineView,
    CourseView,
    CreateCourseView,
    ModuleView,
    CreateModuleView,
    UnitView,
    CreateUnitView,
)

urlpatterns = [
    path("", InstituteView.as_view(), name="home"),
    path("institute/", InstituteView.as_view(), name="institute"),
    path(
        "institute/add/", CreateInstituteView.as_view(), name="create-institute"
    ),
    path("level/", LevelView.as_view(), name="level"),
    path("level/add/", CreateLevelView.as_view(), name="create-level"),
    path("programme/", ProgrammeView.as_view(), name="programme"),
    path(
        "programme/add/", CreateProgrammeView.as_view(), name="create-programme"
    ),
    path("discipline/", DisciplineView.as_view(), name="discipline"),
    path(
        "discipline/add/",
        CreateDisciplineView.as_view(),
        name="create-discipline",
    ),
    path("course/", CourseView.as_view(), name="course"),
    path("course/add/", CreateCourseView.as_view(), name="create-course"),
    path("module/", ModuleView.as_view(), name="module"),
    path("module/add/", CreateModuleView.as_view(), name="create-module"),
    path("unit/", UnitView.as_view(), name="unit"),
    path("unit/add/", CreateUnitView.as_view(), name="create-unit"),
]
