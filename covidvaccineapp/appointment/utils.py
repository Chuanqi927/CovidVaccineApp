from django import template
from .models import Appointment, OfferAppointment
from datetime import datetime


def check_expiration():
    target_offers = OfferAppointment.objects.filter(status="pending")
    # print(target_offers)
    for offer in target_offers:
        if offer.expire_time < datetime.now():
            offer.status = "expired"
            offer.save()
    print("all pending offers have been checked")
