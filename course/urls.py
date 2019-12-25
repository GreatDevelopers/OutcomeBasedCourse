from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", InstituteView.as_view(), name="home"),
    path("institute/", InstituteView.as_view(), name="institute"),
    path(
        "institute/add/", login_required(CreateInstituteView.as_view()), name="create-institute"
    ),
    path("level/", LevelView.as_view(), name="level"),
    path("level/add/", login_required(CreateLevelView.as_view()), name="create-level"),
    path("programme/", ProgrammeView.as_view(), name="programme"),
    path(
        "programme/add/", login_required(CreateProgrammeView.as_view()), name="create-programme"
    ),
    path("discipline/", DisciplineView.as_view(), name="discipline"),
    path(
        "discipline/add/",
        login_required(CreateDisciplineView.as_view()),
        name="create-discipline",
    ),
    path("course/", CourseView.as_view(), name="course"),
    path("syllabus/<str:course_id>", SyllabusView.as_view(), name="syllabus"),
    path("course/add/", login_required(CreateCourseView.as_view()), name="create-course"),
    path("module/", ModuleView.as_view(), name="module"),
    path("module/add/", login_required(CreateModuleView.as_view()), name="create-module"),
    path("unit/", UnitView.as_view(), name="unit"),
    path("unit/add/", login_required(CreateUnitView.as_view()), name="create-unit"),
]
