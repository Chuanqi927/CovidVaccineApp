# Generated by Django 3.1.2 on 2021-04-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityGroup',
            fields=[
                ('group_number', models.AutoField(primary_key=True, serialize=False)),
                ('eligible_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyTimeSlot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('weekday', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
