from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("app/", include(("app.urls", "app"), namespace="app")),
    path('admin/', admin.site.urls),
]
