from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Patient, Provider
from staticInfo.models import WeeklyTimeSlot, PriorityGroup
from django.core.exceptions import ValidationError


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
        patient.max_distance_preferences = 50
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


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#
# class PatientUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['phone_number', 'address_line1', 'address_line2', 'city', 'state',
#                   'country', 'zipcode']
#
#
class PatientUpdatePreferenceForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['max_distance_preferences']


class PatientUpdateProfileForm(forms.Form):
    email = forms.CharField(required=False, label="email")
    phone_number = forms.CharField(required=False, label="phone_number")
    address_line1 = forms.CharField(required=False, label="address_line1")
    address_line2 = forms.CharField(required=False, label="address_line2")
    city = forms.CharField(required=False, label="city")
    state = forms.CharField(required=False, label="state")
    country = forms.CharField(required=False, label="country")
    zipcode = forms.CharField(required=False, label="zipcode")

    @transaction.atomic
    def save(self, user):
        user.email = self.cleaned_data.get("email")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.patient.address_line1 = self.cleaned_data.get("address_line1")
        user.patient.address_line2 = self.cleaned_data.get("address_line2")
        user.patient.city = self.cleaned_data.get("city")
        user.patient.state = self.cleaned_data.get("state")
        user.patient.country = self.cleaned_data.get("country")
        user.patient.zipcode = self.cleaned_data.get("zipcode")
        user.patient.save()
        return user


class PatientUpdateTimePrefForm(forms.Form):
    check1 = forms.BooleanField(required=False, label='check1')
    check2 = forms.BooleanField(required=False)
    check3 = forms.BooleanField(required=False)
    check4 = forms.BooleanField(required=False)
    check5 = forms.BooleanField(required=False)
    check6 = forms.BooleanField(required=False)
    check7 = forms.BooleanField(required=False)
    check8 = forms.BooleanField(required=False)
    check9 = forms.BooleanField(required=False)
    check10 = forms.BooleanField(required=False)
    check11 = forms.BooleanField(required=False)
    check12 = forms.BooleanField(required=False)
    check13 = forms.BooleanField(required=False)
    check14 = forms.BooleanField(required=False)
    check15 = forms.BooleanField(required=False)
    check16 = forms.BooleanField(required=False)
    check17 = forms.BooleanField(required=False)
    check18 = forms.BooleanField(required=False)
    check19 = forms.BooleanField(required=False)
    check20 = forms.BooleanField(required=False)
    check21 = forms.BooleanField(required=False)
    check22 = forms.BooleanField(required=False)
    check23 = forms.BooleanField(required=False)
    check24 = forms.BooleanField(required=False)
    check25 = forms.BooleanField(required=False)
    check26 = forms.BooleanField(required=False)
    check27 = forms.BooleanField(required=False)
    check28 = forms.BooleanField(required=False)
    check29 = forms.BooleanField(required=False)
    check30 = forms.BooleanField(required=False)
    check31 = forms.BooleanField(required=False)
    check32 = forms.BooleanField(required=False)
    check33 = forms.BooleanField(required=False)
    check34 = forms.BooleanField(required=False)
    check35 = forms.BooleanField(required=False)
    check36 = forms.BooleanField(required=False)
    check37 = forms.BooleanField(required=False)
    check38 = forms.BooleanField(required=False)
    check39 = forms.BooleanField(required=False)
    check40 = forms.BooleanField(required=False)
    check41 = forms.BooleanField(required=False)
    check42 = forms.BooleanField(required=False)

    def save(self, patient):
        for i in range(42):
            slot_object = WeeklyTimeSlot.objects.get(slot_id=int(i+1))
            check_str = "check" + str(i+1)
            slot_object.patient.add(patient) if self.cleaned_data.get(
                check_str) else slot_object.patient.remove(patient)
        return patient


class UpdatePasswordForm(forms.Form):
    password_current = forms.CharField(
        label="password_current", widget=forms.PasswordInput
    )
    password_new = forms.CharField(label="password_new", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="password_confirm", widget=forms.PasswordInput
    )

    def __init__(self, user, data=None):
        self.user = user
        super(UpdatePasswordForm, self).__init__(data=data)

    def clean_password_current(self):
        if not self.user.check_password(
                self.cleaned_data.get("password_current", None)
        ):
            raise ValidationError("Current password is incorrect")

    def clean_password_confirm(self):
        password1 = self.cleaned_data.get("password_new")
        password2 = self.cleaned_data.get("password_confirm")

        if password1 and password2 and password1 != password2:
            raise ValidationError("New passwords don't match")

        return self.cleaned_data["password_confirm"]

    def save(self, user, commit=True):
        user.set_password(self.cleaned_data["password_new"])
        user.save()
        return user


class ProviderUpdateProfileForm(forms.Form):
    name = forms.CharField(required=False, label="name")
    providerType = forms.CharField(required=False, label="providerType")
    email = forms.CharField(required=False, label="email")
    address_line1 = forms.CharField(required=False, label="address_line1")
    address_line2 = forms.CharField(required=False, label="address_line2")
    city = forms.CharField(required=False, label="city")
    state = forms.CharField(required=False, label="state")
    country = forms.CharField(required=False, label="country")
    zipcode = forms.CharField(required=False, label="zipcode")

    @transaction.atomic
    def save(self, provider):
        provider.name = self.cleaned_data.get("name")
        provider.providerType = self.cleaned_data.get("providerType")
        provider.email = self.cleaned_data.get("email")
        provider.address_line1 = self.cleaned_data.get("address_line1")
        provider.address_line2 = self.cleaned_data.get("address_line2")
        provider.city = self.cleaned_data.get("city")
        provider.state = self.cleaned_data.get("state")
        provider.country = self.cleaned_data.get("country")
        provider.zipcode = self.cleaned_data.get("zipcode")
        provider.save()
        return provider
