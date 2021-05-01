from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("patient_register/", views.PatientRegister.as_view(), name="patient_register"),
    path("provider_register/", views.ProviderRegister.as_view(), name="provider_register"),
    path("login/", views.login_request, name="login"),
    path("patient_profile/", views.patient_profile, name="patient_profile"),
    path("provider_profile/", views.provider_profile, name="provider_profile"),

    # path(
    #     "provider_register/",
    #     views.provider_register.as_view(),
    #     name="provider_register",
    # ),

    # path("logout/", views.logout_view, name="logout"),
    # path("patient_register/", views.PatientRegister.as_view(), name="patient_register"),
]
