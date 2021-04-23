from django.db import models
from django.conf import settings
import staticInfo.models

# Create your models here.


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    provider_username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="provider_username",
        on_delete=models.CASCADE,
    )
    appointment_time = models.DateTimeField()
    slot_id = models.ForeignKey(
        staticInfo.models.WeeklyTimeSlot,
        on_delete=models.CASCADE,
    )
    available_number = models.IntegerField()

    patient_username = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="patient_username"
    )
    status = models.CharField(max_length=255)
    expire_time = models.DateTimeField()
