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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['phone_number', 'address_line1', 'address_line2', 'city', 'state',
                  'country', 'zipcode']


class PatientUpdatePreferenceForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['max_distance_preferences']


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
        slot_object1 = WeeklyTimeSlot.objects.get(slot_id=1)
        slot_object2 = WeeklyTimeSlot.objects.get(slot_id=2)
        slot_object3 = WeeklyTimeSlot.objects.get(slot_id=3)
        slot_object4 = WeeklyTimeSlot.objects.get(slot_id=4)
        slot_object5 = WeeklyTimeSlot.objects.get(slot_id=5)
        slot_object6 = WeeklyTimeSlot.objects.get(slot_id=6)
        slot_object7 = WeeklyTimeSlot.objects.get(slot_id=7)
        slot_object8 = WeeklyTimeSlot.objects.get(slot_id=8)
        slot_object9 = WeeklyTimeSlot.objects.get(slot_id=9)
        slot_object10 = WeeklyTimeSlot.objects.get(slot_id=10)
        slot_object11 = WeeklyTimeSlot.objects.get(slot_id=11)
        slot_object12 = WeeklyTimeSlot.objects.get(slot_id=12)
        slot_object13 = WeeklyTimeSlot.objects.get(slot_id=13)
        slot_object14 = WeeklyTimeSlot.objects.get(slot_id=14)
        slot_object15 = WeeklyTimeSlot.objects.get(slot_id=15)
        slot_object16 = WeeklyTimeSlot.objects.get(slot_id=16)
        slot_object17 = WeeklyTimeSlot.objects.get(slot_id=17)
        slot_object18 = WeeklyTimeSlot.objects.get(slot_id=18)
        slot_object19 = WeeklyTimeSlot.objects.get(slot_id=19)
        slot_object20 = WeeklyTimeSlot.objects.get(slot_id=20)
        slot_object21 = WeeklyTimeSlot.objects.get(slot_id=21)
        slot_object22 = WeeklyTimeSlot.objects.get(slot_id=22)
        slot_object23 = WeeklyTimeSlot.objects.get(slot_id=23)
        slot_object24 = WeeklyTimeSlot.objects.get(slot_id=24)
        slot_object25 = WeeklyTimeSlot.objects.get(slot_id=25)
        slot_object26 = WeeklyTimeSlot.objects.get(slot_id=26)
        slot_object27 = WeeklyTimeSlot.objects.get(slot_id=27)
        slot_object28 = WeeklyTimeSlot.objects.get(slot_id=28)
        slot_object29 = WeeklyTimeSlot.objects.get(slot_id=29)
        slot_object30 = WeeklyTimeSlot.objects.get(slot_id=30)
        slot_object31 = WeeklyTimeSlot.objects.get(slot_id=31)
        slot_object32 = WeeklyTimeSlot.objects.get(slot_id=32)
        slot_object33 = WeeklyTimeSlot.objects.get(slot_id=33)
        slot_object34 = WeeklyTimeSlot.objects.get(slot_id=34)
        slot_object35 = WeeklyTimeSlot.objects.get(slot_id=35)
        slot_object36 = WeeklyTimeSlot.objects.get(slot_id=36)
        slot_object37 = WeeklyTimeSlot.objects.get(slot_id=37)
        slot_object38 = WeeklyTimeSlot.objects.get(slot_id=38)
        slot_object39 = WeeklyTimeSlot.objects.get(slot_id=39)
        slot_object40 = WeeklyTimeSlot.objects.get(slot_id=40)
        slot_object41 = WeeklyTimeSlot.objects.get(slot_id=41)
        slot_object42 = WeeklyTimeSlot.objects.get(slot_id=42)

        slot_object1.patient.add(patient) if self.cleaned_data.get("check1") else slot_object1.patient.remove(patient)
        slot_object2.patient.add(patient) if self.cleaned_data.get(
            "check2") else slot_object2.patient.remove(patient)
        slot_object3.patient.add(patient) if self.cleaned_data.get(
            "check3") else slot_object3.patient.remove(patient)
        slot_object4.patient.add(patient) if self.cleaned_data.get(
            "check4") else slot_object4.patient.remove(patient)
        slot_object5.patient.add(patient) if self.cleaned_data.get(
            "check5") else slot_object5.patient.remove(patient)
        slot_object6.patient.add(patient) if self.cleaned_data.get(
            "check6") else slot_object6.patient.remove(patient)
        slot_object7.patient.add(patient) if self.cleaned_data.get(
            "check7") else slot_object7.patient.remove(patient)
        slot_object8.patient.add(patient) if self.cleaned_data.get(
            "check8") else slot_object8.patient.remove(patient)
        slot_object9.patient.add(patient) if self.cleaned_data.get(
            "check9") else slot_object9.patient.remove(patient)
        slot_object10.patient.add(patient) if self.cleaned_data.get(
            "check10") else slot_object10.patient.remove(patient)
        slot_object11.patient.add(patient) if self.cleaned_data.get(
            "check11") else slot_object11.patient.remove(patient)
        slot_object12.patient.add(patient) if self.cleaned_data.get(
            "check12") else slot_object12.patient.remove(patient)
        slot_object13.patient.add(patient) if self.cleaned_data.get(
            "check13") else slot_object13.patient.remove(patient)
        slot_object14.patient.add(patient) if self.cleaned_data.get(
            "check14") else slot_object14.patient.remove(patient)
        slot_object15.patient.add(patient) if self.cleaned_data.get(
            "check15") else slot_object15.patient.remove(patient)
        slot_object16.patient.add(patient) if self.cleaned_data.get(
            "check16") else slot_object16.patient.remove(patient)
        slot_object17.patient.add(patient) if self.cleaned_data.get(
            "check17") else slot_object17.patient.remove(patient)
        slot_object18.patient.add(patient) if self.cleaned_data.get(
            "check18") else slot_object18.patient.remove(patient)
        slot_object19.patient.add(patient) if self.cleaned_data.get(
            "check19") else slot_object19.patient.remove(patient)
        slot_object20.patient.add(patient) if self.cleaned_data.get(
            "check20") else slot_object20.patient.remove(patient)
        slot_object21.patient.add(patient) if self.cleaned_data.get(
            "check21") else slot_object21.patient.remove(patient)
        slot_object22.patient.add(patient) if self.cleaned_data.get(
            "check22") else slot_object22.patient.remove(patient)
        slot_object23.patient.add(patient) if self.cleaned_data.get(
            "check23") else slot_object23.patient.remove(patient)
        slot_object24.patient.add(patient) if self.cleaned_data.get(
            "check24") else slot_object24.patient.remove(patient)
        slot_object25.patient.add(patient) if self.cleaned_data.get(
            "check25") else slot_object25.patient.remove(patient)
        slot_object26.patient.add(patient) if self.cleaned_data.get(
            "check26") else slot_object26.patient.remove(patient)
        slot_object27.patient.add(patient) if self.cleaned_data.get(
            "check27") else slot_object27.patient.remove(patient)
        slot_object28.patient.add(patient) if self.cleaned_data.get(
            "check28") else slot_object28.patient.remove(patient)
        slot_object29.patient.add(patient) if self.cleaned_data.get(
            "check29") else slot_object29.patient.remove(patient)
        slot_object30.patient.add(patient) if self.cleaned_data.get(
            "check30") else slot_object30.patient.remove(patient)
        slot_object31.patient.add(patient) if self.cleaned_data.get(
            "check31") else slot_object31.patient.remove(patient)
        slot_object32.patient.add(patient) if self.cleaned_data.get(
            "check32") else slot_object32.patient.remove(patient)
        slot_object33.patient.add(patient) if self.cleaned_data.get(
            "check33") else slot_object33.patient.remove(patient)
        slot_object34.patient.add(patient) if self.cleaned_data.get(
            "check34") else slot_object34.patient.remove(patient)
        slot_object35.patient.add(patient) if self.cleaned_data.get(
            "check35") else slot_object35.patient.remove(patient)
        slot_object36.patient.add(patient) if self.cleaned_data.get(
            "check36") else slot_object36.patient.remove(patient)
        slot_object37.patient.add(patient) if self.cleaned_data.get(
            "check37") else slot_object37.patient.remove(patient)
        slot_object38.patient.add(patient) if self.cleaned_data.get(
            "check38") else slot_object38.patient.remove(patient)
        slot_object39.patient.add(patient) if self.cleaned_data.get(
            "check39") else slot_object39.patient.remove(patient)
        slot_object40.patient.add(patient) if self.cleaned_data.get(
            "check40") else slot_object40.patient.remove(patient)
        slot_object41.patient.add(patient) if self.cleaned_data.get(
            "check41") else slot_object41.patient.remove(patient)
        slot_object42.patient.add(patient) if self.cleaned_data.get(
            "check42") else slot_object42.patient.remove(patient)

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
