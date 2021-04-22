from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
import json


def index(request):
    return HttpResponse("this is user home page")


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
