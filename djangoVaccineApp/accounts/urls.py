from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('customer_register/', views.patient_register.as_view(), name='patient_register'),
    path('employee_register/', views.provider_register.as_view(), name='provider_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
