from django import forms
from .models import Appointment
from staticInfo.models import WeeklyTimeSlot
from user.models import Provider
import pytz
from datetime import datetime
from django.contrib.auth import get_user_model


class AppointmentCreationForm(forms.Form):
    appointment_time = forms.DateTimeField(label="appointment_time")
    available_number = forms.IntegerField()
    slot_id = forms.IntegerField()
    provider_id = forms.IntegerField()

    def calculate_slot_id(self):
        weekday = self.cleaned_data['appointment_time'].isoweekday()
        target_slots = WeeklyTimeSlot.objects.filter(weekday=weekday)
        # print(target_slots)
        timestamp = self.cleaned_data['appointment_time'].strftime('%H:%M')
        # print(timestamp)
        # print("self.time is ", self.cleaned_data['appointment_time'])
        # print(datetime.strptime('12:00', '%H:%M').time() < self.cleaned_data[
        #     'appointment_time'].time() < datetime.strptime('14:00', '%H:%M').time())
        if datetime.strptime('00:00', '%H:%M').time() <= self.cleaned_data[
            'appointment_time'].time() < datetime.strptime('04:00',
                                                                    '%H:%M').time():
            target_slots = target_slots.filter(slot_id__in=[1, 2, 3, 4, 5, 6, 7])
        elif datetime.strptime('04:00', '%H:%M').time() <= self.cleaned_data[
            'appointment_time'].time() < datetime.strptime('08:00',
                                                                    '%H:%M').time():
            target_slots = target_slots.filter(slot_id__in=[8, 9, 10, 11, 12, 13, 14])
        elif datetime.strptime('08:00', '%H:%M').time() <= self.cleaned_data[
            'appointment_time'].time() < datetime.strptime('12:00',
                                                                    '%H:%M').time():
            target_slots = target_slots.filter(slot_id__in=[15, 16, 17, 18, 19, 20, 21])
        elif datetime.strptime('12:00', '%H:%M').time() <= self.cleaned_data[
            'appointment_time'].time() < datetime.strptime('16:00',
                                                                    '%H:%M').time():
            target_slots = target_slots.filter(slot_id__in=[22, 23, 24, 25, 26, 27, 28])
        elif datetime.strptime('16:00', '%H:%M').time() <= self.cleaned_data[
            'appointment_time'].time() < datetime.strptime('20:00',
                                                                    '%H:%M').time():
            target_slots = target_slots.filter(slot_id__in=[29, 30, 31, 32, 33, 34, 35])
        # elif datetime.strptime('20:00', '%H:%M').time() <= self.cleaned_data[
        #     'appointment_time'].time() < datetime.strptime('24:00',
        #                                                             '%H:%M').time():
        #     target_slots = target_slots.filter(slot_id__in=[8, 9, 10, 11, 12, 13, 14])
        else:
            target_slots = target_slots.filter(slot_id__in=[36, 37, 38, 39, 40, 41, 42])
        # print(target_slots)
        self.cleaned_data['slot_id'] = target_slots.values('slot_id')[0].get('slot_id')
        # print(self.cleaned_data['slot_id'])
        return

    def save(self,  commit=True):
        provider = Provider.objects.get(user_id=self.cleaned_data["provider_id"])
        slot_id = WeeklyTimeSlot.objects.get(slot_id=self.cleaned_data["slot_id"])
        appointment = Appointment.objects.create(
            provider=provider,
            appointment_time=self.cleaned_data["appointment_time"],
            slot_id=slot_id,
            available_number=self.cleaned_data["available_number"],
            remaining_number=self.cleaned_data["available_number"],
        )
        return appointment
