# Generated by Django 3.2 on 2021-05-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_patient_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='max_distance_preferences',
            field=models.FloatField(),
        ),
    ]