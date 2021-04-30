from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ssn = models.CharField(max_length=20)
    dob = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    max_distance_preferences = models.FloatField(null=True, default=0)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    group_number = models.ForeignKey(
        "staticInfo.PriorityGroup", on_delete=models.CASCADE
    )


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    providerType = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
