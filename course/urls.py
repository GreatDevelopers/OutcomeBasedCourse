from django.urls import path
from .views import InstituteView, CreateInstituteView

urlpatterns = [
    path(
        "institute/add/", CreateInstituteView.as_view(), name="create-institute"
    ),
    path("", InstituteView.as_view(), name="home"),
]
