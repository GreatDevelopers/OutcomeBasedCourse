from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home_page, name="home"),
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
        login_required(OutcomeFormView.as_view()),
        name="create-outcome",
    ),
    path(
        "outcome/<str:outcome_id>/change/",
        login_required(OutcomeFormView.as_view()),
        name="edit-outcome",
    ),
    path("objective/", ObjectiveView.as_view(), name="objective"),
    path(
        "objective/add/",
        login_required(ObjectiveFormView.as_view()),
        name="create-objective",
    ),
    path(
        "objective/<str:objective_id>/change/",
        login_required(ObjectiveFormView.as_view()),
        name="edit-objective",
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
    path("syllabus/<str:course_id>", SyllabusView.as_view(), name="syllabus"),
    path("course/", CourseView.as_view(), name="course"),
    path(
        "course/add/",
        login_required(CourseFormView.as_view()),
        name="create-course",
    ),
    path(
        "course/<str:course_id>/change/",
        login_required(CourseFormView.as_view()),
        name="edit-course",
    ),
    path("module/", ModuleView.as_view(), name="module"),
    path(
        "module/add/",
        login_required(ModuleFormView.as_view()),
        name="create-module",
    ),
    path(
        "module/<str:module_id>/change/",
        login_required(ModuleFormView.as_view()),
        name="edit-module",
    ),
    path("unit/", UnitView.as_view(), name="unit"),
    path(
        "unit/add/", login_required(UnitFormView.as_view()), name="create-unit"
    ),
    path(
        "unit/<str:unit_number>/change/",
        login_required(UnitFormView.as_view()),
        name="edit-unit",
    ),
    path("printpdf/<str:course_id>", html_to_pdf.as_view(), name="syllabus"),
]
