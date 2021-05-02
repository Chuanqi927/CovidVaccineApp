from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
import json
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .forms import PatientSignUpForm, ProviderSignUpForm, UserUpdateForm, PatientUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Patient, Provider



def register(request):
    return render(request, "register.html")


class PatientRegister(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = "patient_register.html"
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
                return redirect("patient_profile")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        return render(
            request, "login.html", context={"form": AuthenticationForm()}
        )


def logout_view(request):
    logout(request)
    return redirect("homepage")


def provider_profile(request):
    return render(request, "provider_profile.html")


def patient_profile(request):
    # def profile(request):
    #     if request.method == 'POST':
    #         u_form = UserUpdateForm(request.POST, instance=request.user)
    #         p_form = ProfileUpdateForm(request.POST,
    #                                    request.FILES,
    #                                    instance=request.user.profile)
    #         if u_form.is_valid() and p_form.is_valid():
    #             u_form.save()
    #             p_form.save()
    #             messages.success(request, f'Your account has been updated!')
    #             return redirect('profile')
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
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "patient_profile.html", context)





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
#     return render(request, template_name="login.html", context={"form": form})
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
