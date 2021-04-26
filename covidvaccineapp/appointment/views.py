from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return HttpResponse("this is appointment home page")


def upload(request):
    if request.method == "POST":
        print(request.POST)
        # return redirect("../success")
    return render(request, "upload_appointments.html")


def success(request):
    return render(request, "upload_success.html")
