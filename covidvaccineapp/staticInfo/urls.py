from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("slots/", views.show_time_slots, name="slots"),
    path("groups/", views.show_priority_groups, name="groups"),
]
