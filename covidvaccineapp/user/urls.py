from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("test/", views.test, name="test"),
    path("signup/", views.sign_up, name="signup"),
    path(
        "patient_signup/", views.PatientSignUp.as_view(), name="patient_signup"
    ),
    path(
        "provider_register/",
        views.ProviderRegister.as_view(),
        name="provider_register",
    ),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("provider_profile/", views.provider_profile, name="provider_profile"),
    path("patient_profile/", views.patient_profile, name="patient_profile"),
    path("patient_edit_profile/", views.patient_edit_profile, name="patient_edit_profile"),
    path("patient_edit_preference/", views.patient_edit_preference, name="patient_edit_preference"),
    path("patient_edit_timepref/", views.patient_edit_timepref, name="patient_edit_timepref"),
    path("update_password/", views.update_password, name="update_password"),
    path("provider_edit_profile/", views.provider_edit_profile, name="provider_edit_profile"),
    path("admin_profile/", views.admin_profile, name="admin_profile"),
]


