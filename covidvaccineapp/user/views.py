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
from .forms import PatientSignUpForm, PatientLoginForm, PatientProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def patient_login(request):
    if request.user.is_authenticated:
        return redirect("/user")
    else:
        form = PatientLoginForm(request.POST or None)
        context = {"form" : form}
        print(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print("will login")
                login(request, user)
                return redirect("/user/patient_profile")
            else:
                messages.error(request, "Invalid username or password 1")
        else:
            messages.error(request, "Invalid username or password 2")
            print("error")
    return render(request, "patient_login.html", context)


def patient_register(request):
    if request.user.is_authenticated:
        return HttpResponse("You have already logged in.")
    if request.method == "POST":
        print(request.POST)
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            user.is_active = True
            user.save()
            return render(request=request,
                          template_name="registration_success.html")
    else:
        form = PatientSignUpForm()
    return render(request=request, template_name="patient_register.html", context={"form": form})


@login_required(login_url="/user/login")
def patient_profile(request):
    if request.method == "POST":
        print(request.POST)
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            form.save(request.user.id)
            return render(request=request,
                          template_name="registration_success.html")
    else:
        form = PatientProfileForm()
    return render(request=request, template_name="patient_profile.html", context={"form": form})











# class PatientRegister(CreateView):
#     model = User
#     form = PatientSignUpForm
#     template_name = "patient_register.html"
#
#     def form_valid(self, form):
#         print(form)
#         form.save()
#         return render(template_name="registration_success.html")


# def provider_register(request):
#     if request.user.is_authenticated:
#         return redirect("index")
#     if request.method == "POST":
#         print(request.POST)
#         form = ProviderSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.is_active = False
#             user.save()
#             return render(request=request, template_name="registration_success.html")
#     else:
#         return render(request=request, template_name="provider_register.html")



#
#
# def logout_view(request):
#     logout(request)
#     return redirect("/")


# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect("index")
#     if request.method == "POST":
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("user:register")
#     else:
#         form = AuthenticationForm()
#     return render(request, template_name="patient_login.html", context={"form": form})
#
#
# def register(request):
#     if request.user.is_authenticated:
#         return redirect("index")
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.is_active = False
#             user.save()
#             send_verification_email(request, form.cleaned_data.get("email"))
#             return render(request=request, template_name="sent_verification_email.html")
#     else:
#         form = UserCreationForm()
#     return render(
#         request=request, template_name="register.html", context={"form": form}
#     )
#
#
# def post_logout(request):
#     logout(request)
#     return redirect("user:login")
#
#
# def account_details(request):
#     if not request.user.is_authenticated:
#         return redirect("user:login")
#
#     user = request.user
#
#     favorite_restaurant_list = user.favorite_restaurants.all()
#     user_pref_list = user.preferences.all()
#     user_pref_list_json = []
#     for pref in user_pref_list:
#         pref_dic = model_to_dict(pref)
#         user_pref_list_json.append(pref_dic)
#
#     return render(
#         request=request,
#         template_name="account_details.html",
#         context={
#             "favorite_restaurant_list": favorite_restaurant_list,
#             "user_pref": user_pref_list,
#             "user_pref_json": json.dumps(user_pref_list_json, cls=DjangoJSONEncoder),
#         },
#     )
