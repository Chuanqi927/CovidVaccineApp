from django.db import models


# Create your models here.
from covidvaccineapp import staticInfo
from covidvaccineapp import user


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    provider_username = models.ForeignKey('user.AppUser')
    appointment_time = models.DateTimeField()
    slot_id = models.ForeignKey(staticInfo.TimeSlot)
    available_number = models.IntegerField()

    patient_username = models.ManyToManyField('user.AppUser')
    status = models.CharField()
