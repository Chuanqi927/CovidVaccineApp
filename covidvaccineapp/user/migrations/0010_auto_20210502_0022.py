# Generated by Django 3.1.2 on 2021-05-02 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staticInfo', '0002_weeklytimeslot_patient'),
        ('user', '0009_alter_patient_max_distance_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='group_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staticInfo.prioritygroup'),
        ),
    ]
