from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
import json
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .models import User, Patient, Provider
from .forms import PatientSignUpForm, ProviderSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required

from staticInfo.models import PriorityGroup


def index(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")


class PatientRegister(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = "patient_register.html"
    form = PatientSignUpForm()
    print(form)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("patient_profile")


class ProviderRegister(CreateView):
    model = User
    form_class = ProviderSignUpForm
    template_name = "provider_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("provider_profile")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("patient_profile")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(
        request, "login.html", context={"form": AuthenticationForm()}
    )


@login_required(login_url="/user/login")
def patient_profile(request):
    return HttpResponse("this is patient profile")


@login_required(login_url="/user/login")
def provider_profile(request):
    return HttpResponse("this is provider profile")
