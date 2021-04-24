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

    patient = models.ManyToManyField("user.Patient", related_name="patient")
    status = models.CharField(max_length=255)
    expire_time = models.DateTimeField()
