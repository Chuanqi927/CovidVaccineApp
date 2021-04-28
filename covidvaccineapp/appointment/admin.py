from django.contrib import admin
from .models import Appointment, OfferAppointment

# Register your models here.

admin.site.register(Appointment)
admin.site.register(OfferAppointment)
