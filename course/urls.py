from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home_page),
    path(
        "cognitive-level/", CognitiveLevelView.as_view(), name="cognitive-level"
    ),
    path(
        "cognitive-level/add/",
        login_required(CreateCognitiveLevelView.as_view()),
        name="create-cognitive-level",
    ),
    path("action-verb/", ActionVerbView.as_view(), name="action-verb"),
    path(
        "action-verb/add/",
        login_required(CreateActionVerbView.as_view()),
        name="create-action-verb",
    ),
    path("outcome/", OutcomeView.as_view(), name="outcome"),
    path(
        "outcome/add/",
        login_required(CreateOutcomeView.as_view()),
        name="create-outcome",
    ),
    path("objective/", ObjectiveView.as_view(), name="objective"),
    path(
        "objective/add/",
        login_required(CreateObjectiveView.as_view()),
        name="create-objective",
    ),
    path("institute/", InstituteView.as_view(), name="institute"),
    path(
        "institute/add/",
        login_required(InstituteFormView.as_view()),
        name="create-institute",
    ),
    path(
        "institute/<uuid:institute_id>/change/",
        login_required(InstituteFormView.as_view()),
        name="edit-institute",
    ),
    path("level/", LevelView.as_view(), name="level"),
    path(
        "level/add/",
        login_required(LevelFormView.as_view()),
        name="create-level",
    ),
    path(
        "level/<uuid:level_id>/change/",
        login_required(LevelFormView.as_view()),
        name="edit-level",
    ),
    path("programme/", ProgrammeView.as_view(), name="programme"),
    path(
        "programme/add/",
        login_required(ProgrammeFormView.as_view()),
        name="create-programme",
    ),
    path(
        "programme/<str:programme_code>/change/",
        login_required(ProgrammeFormView.as_view()),
        name="edit-programme",
    ),
    path("department/", DepartmentView.as_view(), name="department"),
    path(
        "department/add/",
        login_required(DepartmentFormView.as_view()),
        name="create-department",
    ),
    path(
        "department/<str:department_code>/change/",
        login_required(DepartmentFormView.as_view()),
        name="edit-department",
    ),
    path("discipline/", DisciplineView.as_view(), name="discipline"),
    path(
        "discipline/add/",
        login_required(DisciplineFormView.as_view()),
        name="create-discipline",
    ),
    path(
        "discipline/<str:discipline_code>/change/",
        login_required(DisciplineFormView.as_view()),
        name="edit-discipline",
    ),
    path("course/", CourseView.as_view(), name="course"),
    path("syllabus/<str:course_id>", SyllabusView.as_view(), name="syllabus"),
    path(
        "course/add/",
        login_required(CreateCourseView.as_view()),
        name="create-course",
    ),
    path("module/", ModuleView.as_view(), name="module"),
    path(
        "module/add/",
        login_required(CreateModuleView.as_view()),
        name="create-module",
    ),
    path("unit/", UnitView.as_view(), name="unit"),
    path(
        "unit/add/",
        login_required(CreateUnitView.as_view()),
        name="create-unit",
    ),
]
