from django.db import models
import user.models
from django.conf import settings


# Create your models here.
class WeeklyTimeSlot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    weekday = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    patient_username = models.ManyToManyField(settings.AUTH_USER_MODEL)


class PriorityGroup(models.Model):
    group_number = models.AutoField(primary_key=True)
    eligible_date = models.DateTimeField()
