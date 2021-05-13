from datetime import datetime, timedelta
import math
from operator import itemgetter
from django.contrib.auth import get_user_model
from django.db.models import Exists
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives, send_mail
from django import template
from .models import User, Patient, Provider
from appointment.models import Appointment, OfferAppointment
from staticInfo.models import WeeklyTimeSlot, PriorityGroup

from covidvaccineapp.settings import EMAIL_HOST_USER


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
    available_apps = Appointment.objects.filter(remaining_number__gt=0,
                                                appointment_time__gt=valid_time)
    # print("-------------------------available app-------------------------")
    # print(list(available_apps.values()))
    output = list(available_apps.values())
    return output


def get_eligible_patients_id():
    # only consider the preference of eligible patients
    # eligible patients meet all of the following requirements:
    # 1. eligible for vaccine
    # 2. have not received vaccine
    # 3. have not expired/canceled/miss for more than 2 times
    # print("-------------------------eligible patients-------------------------")
    valid_groups = PriorityGroup.objects.filter(
        eligible_date__lte=datetime.now().date())
    # print(list(valid_groups.values()))
    patient_in_eligible_group = Patient.objects.filter(group_number__in=valid_groups)
    # print(list(patient_in_eligible_group.values()))
    patient_eligible_and_not_received_vaccine = patient_in_eligible_group.filter(
        ~Exists(
            OfferAppointment.objects.filter(patient_id__in=patient_in_eligible_group,
                                            status__in=["accepted", "finished"])))
    output = list(patient_eligible_and_not_received_vaccine.values())
    # print(output)

    for patient_dict in output:
        if OfferAppointment.objects.filter(status__in=["expired", "canceled", "miss"],
                                           patient_id=patient_dict["user_id"]).count() > 2:
            output.remove(patient_dict)
    return output


def get_low_priority_patients_id():
    # we do not consider preference of low priority patients
    # low priority patients meet all of the following requirements:
    # 1. have not meet eligible date for vaccine
    # 2. have not received vaccine

    # Or meet one of the following requirements:
    # 1. patients in eligible group but have expired/canceled/miss for more than 2 times
    # print("-------------------------low priority patients-------------------------")

    target_groups = PriorityGroup.objects.filter(
        eligible_date__gte=datetime.now().date())
    # print(list(target_groups.values()))
    patient_not_received_vaccine = Patient.objects.filter(
        ~Exists(OfferAppointment.objects.filter(status__in=["accepted", "finished"])))
    # print(list(patient_not_received_vaccine.values()))
    bad_patient = patient_not_received_vaccine
    patients_not_received_vaccine_and_not_eligible = patient_not_received_vaccine.filter(
        group_number__in=target_groups)
    # print(list(patients_not_received_vaccine_and_not_eligible.values()))

    for patient in bad_patient:
        # print(patient.user_id)
        if OfferAppointment.objects.filter(status__in=["expired", "canceled", "miss"],
                                           patient_id=patient.user_id).count() <= 3:
            # print("hes not bad")
            bad_patient = bad_patient.exclude(user_id=patient.user_id)
    # print(bad_patient)
    union_of_two = (patients_not_received_vaccine_and_not_eligible | bad_patient).distinct()
    output = list(union_of_two.values())
    # print(output)

    return output


# match will return true if the input appointment satisfies all the preferences of input patient
def match(appointment_id, patient_id):
    appointment = Appointment.objects.get(appointment_id=appointment_id)
    patient = Patient.objects.get(user_id=patient_id)

    patient_slots = WeeklyTimeSlot.objects.filter(patient=patient_id)
    max_distance_pref = patient.max_distance_preferences
    patient_latitude = patient.latitude
    patient_longitude = patient.longitude

    app_slot = appointment.slot_id
    provider_id = appointment.provider_id
    provider_latitude = Provider.objects.get(user_id=provider_id).latitude
    provider_longitude = Provider.objects.get(user_id=provider_id).longitude

    # compute distance referencing online source
    # # Haversine formula example in Python
    # # Author: Wayne Dyck
    # import math
    # def distance(origin, destination):
    #     lat1, lon1 = origin
    #     lat2, lon2 = destination
    #     radius = 6371  # km
    #     dlat = math.radians(lat2 - lat1)
    #     dlon = math.radians(lon2 - lon1)
    #     a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
    #         * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    #     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    #     d = radius * c
    #     return d
    # approximate radius of earth in km
    radius = 6371
    dlat = math.radians(provider_latitude - patient_latitude)
    dlon = math.radians(provider_longitude - patient_longitude)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        math.radians(patient_latitude)) \
        * math.cos(math.radians(provider_latitude)) * math.sin(dlon / 2) * math.sin(
        dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    if distance < max_distance_pref and app_slot in patient_slots:
        return True
    return False


def notify(patient_id, appointment_id):
    print("-------------------------notify-------------------------")

    patient = Patient.objects.get(user_id=patient_id)
    appointment = Appointment.objects.get(appointment_id=appointment_id)
    if appointment.remaining_number > 0:
        offer_object = OfferAppointment.objects.create(
            patient=patient,
            appointment=appointment,
            status="pending",
            expire_time=datetime.now() + timedelta(days=2),
        )
        offer_object.save()
        appointment.remaining_number -= 1
        appointment.save()
        print("have sent appointment ", appointment_id, " to ", patient_id)

        # send notification
        user = User.objects.get(id=patient_id)
        subject = 'Thanks for choosing EasyVaccine'
        message = 'You have received an offer for COVID vaccine appointment. Login to your account to checkout!'
        receiver = user.email
        send_mail(subject, message, EMAIL_HOST_USER, [receiver], fail_silently=False)


# preference_flag is a int variable: 1->consider patients' preference; 0->otherwise
# number is the maximum number of appointment sent to one patient
# find the number of matched appointments of each patient, first assign patient with fewest matches (starting from 1)
def send_invitation(available_app, patient_list, preference_flag, number):
    # print("-------------------------send invitation-------------------------")
    if preference_flag:
        # meaning we are considering the eligible group of patients
        patient_match_count = {}
        patient_received_offer_count = {}

        # compute the match count for each patient to determine who to assign first
        for patient_dict in patient_list:
            for appointment_dict in available_app:
                count = 0
                if match(appointment_dict["appointment_id"], patient_dict["user_id"]):
                    count += 1
            # curr_patient_match_count_dict = {
            #     "user_id": patient_dict["user_id"],
            #     "match_count": count,
            # }
            # patient_match_count.append(curr_patient_match_count_dict)
            # patient_match_count = sorted(patient_match_count, key=itemgetter('match_count'))
            patient_match_count[patient_dict["user_id"]] = count
            dict(sorted(patient_match_count.items(), key=lambda item: item[1]))
            # print(patient_match_count)

        # initialize patient_received_offer_count to 0 for each patient
        for patient_dict in patient_list:
            # curr_patient_received_offer_count_dict = {
            #     "user_id": patient_dict["user_id"],
            #     "received_offer": 0,
            # }
            # patient_received_offer_count.append(curr_patient_received_offer_count_dict)
            # patient_received_offer_count = sorted(patient_received_offer_count, key=itemgetter('received_offer'))
            patient_received_offer_count[patient_dict["user_id"]] = 0
            dict(sorted(patient_received_offer_count.items(), key=lambda item: item[1]))
            # print(patient_received_offer_count)

        # start to sending offers, if have the patient has received offers < number, send
        for appointment_dict in available_app:
            for patient_id, count in patient_match_count.items():
                if count == 0:
                    continue
                if match(appointment_dict["appointment_id"], patient_id):
                    if patient_received_offer_count[patient_id] < number and appointment_dict["remaining_number"] > 0:
                        notify(patient_id, appointment_dict["appointment_id"])
                        patient_received_offer_count[patient_id] += 1
                        appointment_dict["remaining_number"] -= 1

        # there may be patient who unfortunately have not received any offers
        # because no match or the only match has been sent to others
        # so send offers again but no considering their preferences any more
        for appointment_dict in available_app:
            for patient_dict in patient_list:
                if patient_received_offer_count[patient_dict["user_id"]] < number and appointment_dict["remaining_number"] > 0:
                    notify(patient_dict["user_id"], appointment_dict["appointment_id"])
                    patient_received_offer_count[patient_dict["user_id"]] += 1
                    appointment_dict["remaining_number"] -= 1

    else:
        # meaning we are considering the low priority group
        patient_received_offer_count = {}

        # initialize patient_received_offer_count to 0 for each patient
        for patient_dict in patient_list:
            patient_received_offer_count[patient_dict["user_id"]] = 0
            dict(sorted(patient_received_offer_count.items(), key=lambda item: item[1]))
            # print(patient_received_offer_count)

        # start to sending offers, if have the patient has received offers < number, send
        for appointment_dict in available_app:
            for patient_dict in patient_list:
                if patient_received_offer_count[patient_dict["user_id"]] < number and appointment_dict["remaining_number"] > 0:
                    notify(patient_dict["user_id"], appointment_dict["appointment_id"])
                    patient_received_offer_count[patient_dict["user_id"]] += 1
                    appointment_dict["remaining_number"] -= 1


def offer():
    print("-------------------------offer-------------------------")
    available_app = get_available_app()
    eligible_patients = get_eligible_patients_id()
    low_priority_patients = get_low_priority_patients_id()

    print(available_app)
    print(eligible_patients)
    print(low_priority_patients)

    send_invitation(available_app, eligible_patients, 1, 3)
    available_app = get_available_app()
    send_invitation(available_app, low_priority_patients, 0, 3)
