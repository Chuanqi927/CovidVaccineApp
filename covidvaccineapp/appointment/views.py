
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User, Patient, Provider
from .forms import AppointmentCreationForm
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.



def upload(request):
    if request.user.is_authenticated and request.user.is_provider:
        user_id = request.user.id
        # print("user_id :", user_id)
        if request.method == "POST" and Provider.objects.filter(user_id=user_id).exists():
            # print("request.POST :", request.POST)
            if "provider_id" in request.POST \
                    and "appointment_time" in request.POST \
                    and "available_number" in request.POST \
                    and "slot_id" in request.POST:
                upload_appointment_form = AppointmentCreationForm(data=request.POST)
                # print("form created")
                if upload_appointment_form.is_valid():
                    # print(upload_appointment_form)
                    # timezone.activate(upload_appointment_form.cleaned_data['appointment_time'])
                    upload_appointment_form.calculate_slot_id()
                    upload_appointment_form.save()
                    return redirect("success")
        else:
            return render(request, "upload_appointments.html")
    return redirect("homepage")


def success(request):
    return render(request, "upload_success.html")
