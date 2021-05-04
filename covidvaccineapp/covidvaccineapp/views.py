from django.shortcuts import render
from django.http import HttpResponse


# def homepage(request):
#     return render(request, "homepage.html")


def index(request):
    return render(request, "index.html")
#
#
# def index2(request):
#     return render(request, "pulseadmin/index.html")
#
#
# def base(request):
#     return render(request, "base.html")


def home(request):
    return render(request, "home.html")
