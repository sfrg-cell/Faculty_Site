from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("departments/", views.departments, name="departments"),
    path("departments/<int:id>/", views.departments_details,
         name="departments_details"),
    path("programs/", views.programs, name="programs"),
    path("programs/<int:id>/", views.programs_details,
         name="programs_details"),
]
