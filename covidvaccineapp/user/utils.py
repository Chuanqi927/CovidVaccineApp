from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db.models import Exists
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template
from .models import User, Patient, Provider
from appointment.models import Appointment, OfferAppointment
from staticInfo.models import WeeklyTimeSlot, PriorityGroup


def send_reset_password_email(request, email):
    user = User.objects.get(email=email)
    host_name = request.get_host()
    base_url = "http://" + host_name + "/user/reset_password/"
    c = {
        "base_url": base_url,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": PasswordResetTokenGenerator().make_token(user),
    }
    htmltemp = template.loader.get_template("reset_password_template.html")
    html_content = htmltemp.render(c)
    email_subject = "Reset Your EzVaccine Password!"
    email = EmailMultiAlternatives(email_subject, to=[user.email])
    email.attach_alternative(html_content, "text/html")
    return email.send()


def get_available_app():
    # available vaccine appointments are:
    # 1. there are still available number for this appointment id
    # 2. the appointment time are at least 1 day after current date time

    valid_time = datetime.now().date() + timedelta(days=1)
    available_apps = Appointment.objects.filter(remaining_number__gt=0, appointment_time__gt=valid_time)
    print("-------------------------available app-------------------------")
    print(list(available_apps.values()))
    output = list(available_apps.values())
    return output


def get_eligible_patients_id():
    # only consider the preference of eligible patients
    # eligible patients meet all of the following requirements:
    # 1. eligible for vaccine
    # 2. have not received vaccine
    # 3. have not expired/canceled/miss for more than 2 times
    print("-------------------------eligible patients-------------------------")
    valid_groups = PriorityGroup.objects.filter(eligible_date__lte=datetime.now().date())
    print(list(valid_groups.values()))
    patients1 = Patient.objects.filter(group_number__in=valid_groups)
    print(list(patients1.values()))
    patients2 = patients1.filter(~Exists(OfferAppointment.objects.filter(patient_id__in=patients1, status__in=["accepted", "finished"])))
    output = list(patients2.values())
    print(output)

    for patient_dict in output:
        if OfferAppointment.objects.filter(status__in=["expired", "canceled", "miss"], patient_id=patient_dict["user_id"]).count() > 2:
            output.remove(patient_dict)
    return output


def get_low_priority_patients_id():
    # we do not consider preference of low priority patients
    # low priority patients meet all of the following requirements:
    # 1. have not meet eligible date for vaccine
    # 2. have not received vaccine

    # Or meet one of the following requirements:
    # 1. patients in eligible group but have expired/canceled/miss for more than 2 times
    print("-------------------------low priority patients-------------------------")

    valid_groups = PriorityGroup.objects.filter(eligible_date__gte=datetime.now().date())
    print(list(valid_groups.values()))
    patients1 = Patient.objects.filter(group_number__in=valid_groups)
    print(list(patients1.values()))
    patients2 = patients1.filter(~Exists(OfferAppointment.objects.filter(patient_id__in=patients1, status__in=["accepted", "finished"])))
    print(list(patients2.values()))
    patients2_list = list(patients2.values())
    for patient_dict in patients2_list:
        if OfferAppointment.objects.filter(status__in=["expired", "canceled", "miss"], patient_id=patient_dict["user_id"]).count() > 2:
            patients2_list.append(patient_dict)
    patients3 = patients2.filter(user_id__in=OfferAppointment.objects.filter(status__in=["expired", "canceled", "miss"]))
    # output =
    # print(output)

    return output


def offer():
    print("-------------------------offer-------------------------")
    available_app = get_available_app()
    eligible_patients = get_eligible_patients_id()
    # low_priority_patients = get_low_priority_patients_id()

    # print(available_app)
    # print(eligible_patients)