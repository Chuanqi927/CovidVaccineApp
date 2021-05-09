from dateutil.relativedelta import relativedelta
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.core.mail import send_mail
from covidvaccineapp.settings import EMAIL_HOST_USER
from datetime import datetime
import json
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .forms import PatientSignUpForm, ProviderSignUpForm, PatientUpdateProfileForm, \
    UpdatePasswordForm, ProviderUpdateProfileForm, PatientUpdateTimePrefForm, \
    PatientUpdatePreferenceForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Patient, Provider
from staticInfo.models import WeeklyTimeSlot, PriorityGroup
from appointment.models import Appointment, OfferAppointment
from appointment.utils import check_expiration
from .utils import offer
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
                elif user.is_superuser:
                    return redirect("admin_profile")
                else:
                    return redirect("home")
        messages.error(request, "Invalid username or password")
    return render(
        request, "login.html", context={"form": AuthenticationForm()}
    )


def logout_view(request):
    logout(request)
    return redirect("home")


def patient_profile(request):
    global context
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    patient = Patient.objects.get(user=user)
    if request.method == 'POST':
        if "email" in request.POST:
            form = PatientUpdateProfileForm(data=request.POST)
            # print("patient update profile form generated")
            if form.is_valid():
                # print("form is valid")
                form.save(user)
                messages.success(request, f"Your information has been updated!")
                return redirect("patient_profile")
        elif "max_distance_preferences" in request.POST:
            pp_form = PatientUpdatePreferenceForm(request.POST, instance=request.user.patient)
            if pp_form.is_valid():
                pp_form.save()
                messages.success(request, f"Your preference has been updated!")
                return redirect("patient_profile")

    check_expiration()
    all_offer = OfferAppointment.objects.filter(patient_id=request.user.id)
    # print(all_offer)
    all_appointment = Appointment.objects.filter(appointment_id__in=all_offer.values_list('appointment'))
    # print(all_appointment)
    all_provider = Provider.objects.filter(user_id__in=all_appointment.values_list('provider_id'))
    # print(all_provider)
    offer_list = list(all_offer.values())
    offered_appointment_list = list(all_appointment.values())
    all_provider_list = list(all_provider.values())

    for i in range(len(offer_list)):
        if offer_list[i]["expire_time"] is None:
            offer_list[i]["expire_time"] = datetime.now()
        offer_list[i]["expire_time"] = offer_list[i]["expire_time"].strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(offered_appointment_list)):
        offered_appointment_list[i]["appointment_time"] = offered_appointment_list[i]["appointment_time"].strftime("%Y-%m-%d %H:%M:%S")
    # print(offer_list)
    # print(offered_appointment)
    for i in range(len(all_provider_list)):
        if all_provider_list[i]["longitude"] is None or all_provider_list[i]["latitude"] is None:
            # assign 6 MetroTech Center's longitude and latitude
            all_provider_list[i]["longitude"] = "40.693710"
            all_provider_list[i]["latitude"] = "-73.987221"
        all_provider_list[i]["longitude"] = str(all_provider_list[i]["longitude"])
        all_provider_list[i]["latitude"] = str(all_provider_list[i]["latitude"])

    all_time_slots_info = get_time_slot_info()
    # print(all_time_slots_info)
    patient = Patient.objects.get(user=request.user)
    saved_slots = list(WeeklyTimeSlot.objects.filter(patient=patient).values())
    for i in range(len(saved_slots)):
        saved_slots[i]["start_time"] = saved_slots[i]["start_time"].strftime("%H:%M:%S")
        saved_slots[i]["end_time"] = saved_slots[i]["end_time"].strftime("%H:%M:%S")
    # print(saved_slots)

    username = request.user.username
    pp_form = PatientUpdatePreferenceForm()
    context = {
        "email": user.email,
        "phone_number": patient.phone_number,
        "address_line1": patient.address_line1,
        "address_line2": patient.address_line2,
        "city": patient.city,
        "state": patient.state,
        "country": patient.country,
        "zipcode": patient.zipcode,
        "username": username,
        "offer_list": offer_list,
        "appointment_list": offered_appointment_list,
        "all_time_slots_info": all_time_slots_info,
        "saved_slots": saved_slots,
        "pp_form": pp_form,
        "user": user,
        "all_provider_list": all_provider_list,
    }
    return render(request, "patient_profile.html", context)


def patient_respond(request, offer_app_id, status):
    if not request.user.is_patient or not Patient.objects.filter(user_id=int(request.user.id)).exists():
        messages.error(request, "You are not authorized")
        return redirect("home")
    target_offer = OfferAppointment.objects.get(id=offer_app_id)
    if target_offer.patient_id != request.user.id:
        messages.error(request, "You are not authorized")
        return redirect("home")
    target_offer.status = status
    target_offer.save()
    messages.success(request, "Your response has been saved")
    return redirect("patient_profile")


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
    # total_upload_appointment_count = all_uploaded_appointments.count()
    # print(all_uploaded_appointments)
    all_uploaded_appointments_list = list(all_uploaded_appointments.values())
    all_offer_appointments = OfferAppointment.objects.filter(appointment_id__in=all_uploaded_appointments)
    # print(all_offer_appointments)
    all_offer_appointments_list = list(all_offer_appointments.values())
    all_accepted_appointments = all_offer_appointments.filter(status="accepted")
    # print(all_accepted_appointments)
    all_accepted_appointments_list = list(all_accepted_appointments.values())

    for i in range(len(all_uploaded_appointments_list)):
        all_uploaded_appointments_list[i]["appointment_time"] = all_uploaded_appointments_list[i]["appointment_time"].strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(all_offer_appointments_list)):
        if all_offer_appointments_list[i]["expire_time"] is None:
            all_offer_appointments_list[i]["expire_time"] = datetime.now()
        all_offer_appointments_list[i]["expire_time"] = all_offer_appointments_list[i]["expire_time"].strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(all_accepted_appointments_list)):
        if all_accepted_appointments_list[i]["expire_time"] is None:
            all_accepted_appointments_list[i]["expire_time"] = datetime.now()
        all_accepted_appointments_list[i]["expire_time"] = all_accepted_appointments_list[i]["expire_time"].strftime("%Y-%m-%d %H:%M:%S")

    total_upload_count = 0
    for uploaded_appointment in all_uploaded_appointments:
        total_upload_count += uploaded_appointment.available_number
    if total_upload_count == 0:
        acceptance_rate = 0
        offer_rate = 0
    else:
        acceptance = all_offer_appointments.filter(status__in=["accepted", "finished"])
        acceptance_rate = 100 * float(acceptance.count()) / float(total_upload_count)
        offer_rate = 100*float(all_offer_appointments.count()) / float(total_upload_count)
        # print(float(acceptance.count()))
        # print(float(all_offer_appointments.count()))
        # print(float(total_upload_count))
        offer_rate = round(offer_rate, 2)
        acceptance_rate = round(acceptance_rate, 2)

    patient_user = User.objects.filter(id__in=all_offer_appointments.values_list('patient_id'))
    # print(patient_user)
    patient_user_list = list(patient_user.values())
    for i in range(len(patient_user_list)):
        patient_user_list[i]["last_login"] = patient_user_list[i]["last_login"].strftime("%Y-%m-%d %H:%M:%S")
        patient_user_list[i]["date_joined"] = patient_user_list[i]["date_joined"].strftime("%Y-%m-%d")
        patient_user_list[i]["is_superuser"] = "false"
        patient_user_list[i]["is_staff"] = "false"
        patient_user_list[i]["is_active"] = "true"
        patient_user_list[i]["is_patient"] = "true"
        patient_user_list[i]["is_provider"] = "false"

    parameter_dict = {
        "email": user.email,
        "name": provider.name,
        "providerType": provider.providerType,
        "address_line1": provider.address_line1,
        "address_line2": provider.address_line2,
        "city": provider.city,
        "state": provider.state,
        "country": provider.country,
        "zipcode": provider.zipcode,
        "all_uploaded_appointments": all_uploaded_appointments_list,
        "all_offer_appointments": all_offer_appointments_list,
        "all_accepted_appointments": all_accepted_appointments_list,
        "user": user,
        "total_upload_count": total_upload_count,
        "offer_rate": offer_rate,
        "acceptance_rate": acceptance_rate,
        "patient_user_list": patient_user_list,
    }

    return render(request, "provider_profile.html", context=parameter_dict)


def provider_respond(request, offer_app_id, status):
    if not request.user.is_provider or not Provider.objects.filter(user_id=int(request.user.id)).exists():
        messages.error(request, "You are not authorized")
        return redirect("home")
    target_offer = OfferAppointment.objects.get(id=offer_app_id)
    target_appointment = Appointment.objects.get(appointment_id=target_offer.appointment_id)

    if target_appointment.provider_id != request.user.id:
        messages.error(request, "You are not authorized")
        return redirect("home")
    target_offer.status = status
    target_offer.save()
    messages.success(request, "Your response has been saved")
    return redirect("provider_profile")


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


def admin_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_superuser:
        return HttpResponse("You are not admin")
    patients = Patient.objects.all().values()
    patient_list = list(patients)
    patient_user_list = list(User.objects.filter(is_patient=True).values())
    for i in range(len(patient_list)):
        patient_list[i]["dob"] = patient_list[i]["dob"].strftime("%Y-%m-%d")
        if patient_list[i]["longitude"] is None or patient_list[i]["latitude"] is None:
            # assign 6 MetroTech Center's longitude and latitude
            patient_list[i]["longitude"] = "40.693710"
            patient_list[i]["latitude"] = "-73.987221"
        patient_list[i]["longitude"] = str(patient_list[i]["longitude"])
        patient_list[i]["latitude"] = str(patient_list[i]["latitude"])
    for i in range(len(patient_user_list)):
        patient_user_list[i]["last_login"] = patient_user_list[i]["last_login"].strftime("%Y-%m-%d %H:%M:%S")
        patient_user_list[i]["date_joined"] = patient_user_list[i]["date_joined"].strftime("%Y-%m-%d")
        patient_user_list[i]["is_superuser"] = "false"
        patient_user_list[i]["is_staff"] = "false"
        patient_user_list[i]["is_active"] = "true"
        patient_user_list[i]["is_patient"] = "true"
        patient_user_list[i]["is_provider"] = "false"
    # print(patient_list)
    # print(patient_user_list)
    parameter_dict = {
        "patient_list": patient_list,
        "user_list": patient_user_list,
        "curr_user": request.user,
    }
    return render(request, "admin_profile.html", context=parameter_dict)


def assign_priority(request, patient_id, group_number):
    if not request.user.is_superuser:
        messages.error(request, "You are not admin")
        return redirect("home")
    if Patient.objects.filter(user_id=int(patient_id)).exists():
        target = Patient.objects.get(user_id=patient_id)
        # print(target)
        group = PriorityGroup.objects.get(group_number=group_number)
        # print(group)
        target.group_number = group
        target.save()
        messages.success(request, "Priority Assigned Successfully!")
    return redirect("admin_profile")


def start_offer(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_superuser:
        return HttpResponse("You are not admin")
    offer()
    messages.success(request, "You have turned on offer algorithm to sending available appointments!")
    return redirect("admin_profile")


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


def patient_edit_profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = PatientUpdateForm(request.POST, instance=request.user.patient)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f"Your information has been updated!")
    #         return redirect("patient_profile")
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = PatientUpdateForm(instance=request.user.patient)
    #
    # first_name = request.user.first_name
    # last_name = request.user.last_name
    # username = request.user.username
    #
    # u_form = UserUpdateForm(instance=request.user)
    # p_form = PatientUpdateForm(instance=request.user)
    # context2 = {
    #     "first_name": first_name,
    #     "last_name": last_name,
    #     "username": username,
    #     "u_form": u_form,
    #     "p_form": p_form,
    # }

    return render(request, "patient_edit_profile.html")


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