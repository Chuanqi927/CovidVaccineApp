from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Patient, Provider


class PatientSignUpForm(UserCreationForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address_Line1 = forms.CharField(required=True)
    ssn = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.firstName = self.cleaned_data.get('firstName')
        patient.lastName = self.cleaned_data.get('lastName')
        patient.phone_number = self.cleaned_data.get('phone_number')
        patient.address_Line1 = self.cleaned_data.get('address_Line1')
        patient.ssn = self.cleaned_data.get('ssn')
        patient.save()
        return user


class ProviderSignUpForm(UserCreationForm):

    name = forms.CharField(required=True)
    addressLine1 = forms.CharField(required=True)
    providerType = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.save()
        provider = Provider.objects.create(user=user)

        provider.name = self.cleaned_data.get('name')
        provider.phone_number = self.cleaned_data.get('phone_number')
        provider.providerType = self.cleaned_data.get('providerType')
        provider.save()
        return user