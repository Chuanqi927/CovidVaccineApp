# Generated by Django 3.2 on 2021-05-01 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staticInfo', '0002_weeklytimeslot_patient'),
        ('user', '0007_patient_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='group_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staticInfo.prioritygroup'),
        ),
    ]
