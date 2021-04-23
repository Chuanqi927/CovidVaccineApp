# Generated by Django 3.1.2 on 2021-04-23 00:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("staticInfo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="weeklytimeslot",
            name="patient_username",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
