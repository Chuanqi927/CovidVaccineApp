# Generated by Django 3.1.2 on 2021-04-26 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='max_distance_preferences',
        ),
    ]
