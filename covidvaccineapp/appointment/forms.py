from django import forms


class AppointmentCreationForm(forms.Form):
    appointment_time = forms.DateTimeField(label="appointment_time")
    available_number = forms.IntegerField()
    slot_id = forms.IntegerField()
    provider_id = forms.IntegerField()