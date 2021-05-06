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
    ProviderUpdateProfileForm, PatientUpdateTimePrefForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Patient, Provider
from staticInfo.models import WeeklyTimeSlot
from appointment.models import OfferAppointment, Appointment

from appointment.models import Appointment, OfferAppointment

from staticInfo.utils import get_time_slot_info


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

    u_form = UserUpdateForm(instance=request.user)
    p_form = PatientUpdateForm(instance=request.user)
    context2 = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(request, "patient_edit_profile.html", context2)


def test(request):
    a_list = list(Appointment.objects.prefetch_related('provider'))
    # offer_list = list(OfferAppointment.objects.filter(patient_id=41))
    offer = OfferAppointment.objects.filter(patient_id=41)
    appointment = offer.appointment
    provider = appointment.provider
    list_para = {
        "a_list": a_list,
        "offer_list": list(offer),
        "appointment_list": list(appointment),
        "provider_list": list(provider),

    }

    return render(request, "test.html", context=list_para)


def patient_profile(request):
    global context
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PatientUpdateForm(request.POST, instance=request.user.patient)
        # pp_form = PatientUpdatePreferenceForm(request.POST, instance=request.user.patient)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your information has been updated!")
            return redirect("patient_profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PatientUpdateForm(instance=request.user.patient)
        # pp_form = PatientUpdatePreferenceForm(instance=request.user.patient)

        if request.method == 'POST':
            pp_form = PatientUpdatePreferenceForm(request.POST, instance=request.user.patient)
            if pp_form.is_valid():
                pp_form.save()
                messages.success(request, f"Your preference has been updated!")
                return redirect("patient_profile")
        else:
            pp_form = PatientUpdatePreferenceForm(instance=request.user.patient)

    offer = OfferAppointment.objects.filter(patient_id=request.user.id)
    # print(offer)

    appointment = Appointment.objects.filter(appointment_id__in=offer)
    # provider = Provider.objects.filter(provider)
    offer_list = list(offer)
    # print(offer_list)
    appointment_list = list(appointment)

    all_time_slots_info = get_time_slot_info()
    # print(all_time_slots_info)
    patient = Patient.objects.get(user=request.user)
    saved_slots = list(WeeklyTimeSlot.objects.filter(patient=patient).values())
    for i in range(len(saved_slots)):
        saved_slots[i]["start_time"] = saved_slots[i]["start_time"].strftime("%H:%M:%S")
        saved_slots[i]["end_time"] = saved_slots[i]["end_time"].strftime("%H:%M:%S")
    # print(saved_slots)

    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    u_form = UserUpdateForm(instance=request.user)
    p_form = PatientUpdateForm(instance=request.user)
    pp_form = PatientUpdatePreferenceForm(instance=request.user)
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "pp_form": pp_form,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "offer_list": offer,
        "appointment_list": appointment_list,
        "all_time_slots_info": all_time_slots_info,
        "saved_slots": saved_slots,
    }

    return render(request, "patient_profile.html", context)


def patient_edit_preference(request):
    # if request.method == 'POST':
    #     pp_form = PatientUpdatePreferenceForm(request.POST, instance=request.user.patient)
    #     if pp_form.is_valid():
    #         pp_form.save()
    #         messages.success(request, f"Your preference has been updated!")
    #         return redirect("patient_profile")
    # else:
    #     pp_form = PatientUpdatePreferenceForm(instance=request.user.patient)

    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    contextpp = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,

    }
    return render(request, "patient_edit_preference.html", contextpp)


def patient_edit_timepref(request):
    if request.method == "POST":
        form = PatientUpdateTimePrefForm(data=request.POST)
        # print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save(request.user.patient)
            messages.success(request, "time preference saved!")
    return redirect('patient_profile')


def provider_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    provider = Provider.objects.get(user=user)
    all_uploaded_appointments = Appointment.objects.filter(provider=provider)
    # print(all_uploaded_appointments.count())

    all_offer_appointments = OfferAppointment.objects.filter(appointment_id__in=all_uploaded_appointments)
    print(all_offer_appointments)
    parameter_dict = {
        "email": user.email,
        "name": provider.name,
        "providerType": provider.providerType,
        "address_line1": provider.address_line1,
        "address_line2": provider.address_line2,
        "city": provider.city,
        "country": provider.country,
        "zipcode": provider.zipcode,
        "all_uploaded_appointments": all_uploaded_appointments,
        "all_offer_appointments": all_offer_appointments,
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
        error_context = {"status": "400", "errors": error_list}
        response = HttpResponse(json.dumps(error_context), content_type="application/json")
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
        error_context = {"status": "400", "errors": error_list}
        response = HttpResponse(json.dumps(error_context), content_type="application/json")
        response.status_code = 400
        return response

