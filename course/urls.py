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
]
