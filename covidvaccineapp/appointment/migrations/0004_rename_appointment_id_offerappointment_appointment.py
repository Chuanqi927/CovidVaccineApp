# Generated by Django 3.2 on 2021-05-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment_remaining_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerappointment',
            old_name='appointment_id',
            new_name='appointment',
        ),
    ]