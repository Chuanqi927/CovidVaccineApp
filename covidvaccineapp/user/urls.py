from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path("login", views.user_login, name="login"),
    # path("logout", views.post_logout, name="logout"),
    # path("register", views.register, name="register"),
    # path("account_details", views.account_details, name="account_details"),

]
