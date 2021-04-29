# Generated by Django 3.1.2 on 2021-04-24 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("appointment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="patient",
            field=models.ManyToManyField(related_name="patient", to="user.Patient"),
        ),
        migrations.AddField(
            model_name="appointment",
            name="provider",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="provider",
                to="user.provider",
            ),
        ),
    ]