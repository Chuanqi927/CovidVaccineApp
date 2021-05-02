from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Patient, Provider
from staticInfo.models import PriorityGroup


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    ssn = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    address_line1 = forms.CharField(required=True)
    address_line2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)

    # max_distance_preference = forms.FloatField(min_value=0)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()

        patient = Patient.objects.create(user=user)
        patient.phone_number = self.cleaned_data.get("phone_number")
        patient.address_line1 = self.cleaned_data.get("address_line1")
        patient.address_line2 = self.cleaned_data.get("address_line2")
        patient.ssn = self.cleaned_data.get("ssn")
        patient.dob = self.cleaned_data.get("dob")
        patient.city = self.cleaned_data.get("city")
        patient.state = self.cleaned_data.get("state")
        # patient.max_distance_preferences = 50
        patient.zipcode = self.cleaned_data.get("zipcode")
        patient.country = self.cleaned_data.get("country")
        patient.group_number = PriorityGroup.objects.get(group_number=6)

        patient.save()
        return user


class ProviderSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    providerType = forms.CharField(required=True)
    email = forms.CharField(required=True)
    address_line1 = forms.CharField(required=True)
    address_line2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_provider = True
        user.email = self.cleaned_data.get("email")
        user.save()
        provider = Provider.objects.create(user=user)
        provider.name = self.cleaned_data.get("name")
        provider.phone_number = self.cleaned_data.get("phone_number")
        provider.providerType = self.cleaned_data.get("providerType")
        provider.address_line1 = self.cleaned_data.get("address_line1")
        provider.address_line2 = self.cleaned_data.get("address_line2")
        provider.city = self.cleaned_data.get("city")
        provider.state = self.cleaned_data.get("state")
        provider.country = self.cleaned_data.get("country")
        provider.zipcode = self.cleaned_data.get("zipcode")
        provider.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['max_distance_preferences']
