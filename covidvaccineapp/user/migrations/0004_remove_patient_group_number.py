# Generated by Django 3.2 on 2021-04-30 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210430_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='group_number',
        ),
    ]