from django.db import models

import staticInfo.models


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(
        "user.Provider",
        related_name="provider",
        on_delete=models.CASCADE,
        default=1,
    )
    appointment_time = models.DateTimeField()
    slot_id = models.ForeignKey(
        staticInfo.models.WeeklyTimeSlot,
        on_delete=models.CASCADE,
    )
    available_number = models.IntegerField()
    remaining_number = models.IntegerField(blank=True, null=True)
    patient = models.ManyToManyField("user.Patient", related_name="patient", through='OfferAppointment')


class OfferAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey("user.Patient", on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True, default=None)
    expire_time = models.DateTimeField()




