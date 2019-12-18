from django.urls import path
from .views import (
    InstituteView,
    CreateInstituteView,
    LevelView,
    CreateLevelView,
)

urlpatterns = [
    path("", InstituteView.as_view(), name="home"),
    path("institute/", InstituteView.as_view(), name="institute"),
    path(
        "institute/add/", CreateInstituteView.as_view(), name="create-institute"
    ),
    path("level/", LevelView.as_view(), name="level"),
    path("level/add/", CreateLevelView.as_view(), name="create-level"),
]
