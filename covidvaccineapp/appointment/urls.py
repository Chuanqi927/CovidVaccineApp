from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("success", views.success, name="success"),
    # path("upload_appointment", views.upload_app, name="upload_app"),
]