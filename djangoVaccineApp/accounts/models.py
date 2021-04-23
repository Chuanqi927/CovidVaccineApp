from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    addressLine1 = models.CharField(max_length=20)
    ssn = models.CharField(max_length=20)


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    addressLine = models.CharField(max_length=100)
    providerType = models.CharField(max_length=20)
