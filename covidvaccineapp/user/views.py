from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
import json
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .forms import PatientSignUpForm, ProviderSignUpForm, UserUpdateForm, \
    PatientUpdateForm, PatientUpdatePreferenceForm, UpdatePasswordForm, \
    ProviderUpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Patient, Provider
from staticInfo.models import WeeklyTimeSlot


def sign_up(request):
    return render(request, "signup.html")


class PatientSignUp(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = "patient_signup.html"
    form = PatientSignUpForm()

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
                if user.is_patient:
                    return redirect("patient_profile")
                elif user.is_provider:
                    return redirect("provider_profile")
                else:
                    return redirect("home")
        messages.error(request, "Invalid username or password")
    return render(
        request, "login.html", context={"form": AuthenticationForm()}
    )


def logout_view(request):
    logout(request)
    return redirect("home")


def patient_edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PatientUpdateForm(request.POST, instance=request.user.patient)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your information has been updated!")
            return redirect("patient_profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PatientUpdateForm(instance=request.user.patient)

        first_name = request.user.first_name
        last_name = request.user.last_name
        username = request.user.username
        context = {
            "u_form": u_form,
            "p_form": p_form,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
        }

        return render(request, "patient_edit_profile.html", context)


def patient_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,

    }
    return render(request, "patient_profile.html", context)


def patient_edit_preference(request):
    if request.method == 'POST':
        pp_form = PatientUpdatePreferenceForm(request.POST, instance=request.user.patient)
        if pp_form.is_valid():
            pp_form.save()
            messages.success(request, f"Your preference has been updated!")
            return redirect("patient_profile")
    else:
        pp_form = PatientUpdatePreferenceForm(instance=request.user.patient)

    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "pp_form": pp_form,


    }
    return render(request, "patient_edit_preference.html", context)


def provider_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    provider = Provider.objects.get(user=user)
    parameter_dict = {
        "email": user.email,
        "name": provider.name,
        "providerType": provider.providerType,
        "address_line1": provider.address_line1,
        "address_line2": provider.address_line2,
        "city": provider.city,
        "country": provider.country,
        "zipcode": provider.zipcode,
    }

    return render(request, "provider_profile.html", context=parameter_dict)


def update_password(request):
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    if request.method == "POST":
        form = UpdatePasswordForm(user=user, data=request.POST)
        if form.is_valid():
            print("new password: ", form.cleaned_data.get("password_new"))
            form.save(user)
            return redirect("login")

        error_list = []
        for field in form:
            for error in field.errors:
                error_list.append(error)
        context = {"status": "400", "errors": error_list}
        response = HttpResponse(json.dumps(context), content_type="application/json")
        response.status_code = 400
        return response


def provider_edit_profile(request):
    if request.method == 'POST':
        form = ProviderUpdateProfileForm(data=request.POST)
        if form.is_valid():
            form.save(request.user.provider)
            messages.success(request, f"Your profile has been updated!")
            return redirect("provider_profile")
        error_list = []
        for field in form:
            for error in field.errors:
                error_list.append(error)
        context = {"status": "400", "errors": error_list}
        response = HttpResponse(json.dumps(context), content_type="application/json")
        response.status_code = 400
        return response

