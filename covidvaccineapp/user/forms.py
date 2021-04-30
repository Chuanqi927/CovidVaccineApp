from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Patient, Provider
from django.contrib.auth.forms import AuthenticationForm


class PatientSignUpForm(UserCreationForm):
    username = forms.CharField(label="Enter Username", min_length=4, max_length=150)
    email = forms.EmailField(label="Enter email")
    password1 = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if not email:
            raise ValidationError("Email is required")
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    @transaction.atomic
    def save(self):
        user = super(PatientSignUpForm, self).save(commit=False)
        user.is_customer = True
        user.username = self.cleaned_data.get("username")
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.is_patient = True
        user.save()

        return user


class PatientLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PatientProfileForm(forms.Form):
    ssn = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    phone_number = forms.CharField(required=True)
    address_line1 = forms.CharField(required=True)
    address_line2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)

    def save(self, user_id):
        patient = Patient.objects.create(
            user_id=user_id,
            ssn=self.cleaned_data.get("ssn"),
            dob=self.cleaned_data.get("dob"),
            phone_number=self.cleaned_data.get("phone_number"),
            address_line1=self.cleaned_data.get("address_line1"),
            address_line2=self.cleaned_data.get("address_line2"),
            city=self.cleaned_data.get("city"),
            country=self.cleaned_data.get("country"),
            zipcode=self.cleaned_data.get("zipcode"),
        )
        patient.save()


class ProviderSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    addressLine1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
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

        provider.name = self.cleaned_data.get("name")
        provider.phone_number = self.cleaned_data.get("phone_number")
        provider.providerType = self.cleaned_data.get("providerType")
        provider.save()
        return user
