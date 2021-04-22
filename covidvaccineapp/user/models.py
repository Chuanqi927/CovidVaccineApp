from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

PriorityGroup = apps.get_model('staticInfo', 'PriorityGroup')


class AppUser(AbstractUser):
    is_patient = models.BooleanField()
    ssn = models.IntegerField
    dob = models.DateTimeField()
    phone = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    max_distance_preferences = models.FloatField()
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True,
                                    null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True,
                                   null=True)
    group_number = models.ForeignKey(PriorityGroup, on_delete=models.CASCADE)

    is_provider = models.BooleanField()
    name = models.CharField(max_length=255)
    providerType = models.CharField(max_length=255)

