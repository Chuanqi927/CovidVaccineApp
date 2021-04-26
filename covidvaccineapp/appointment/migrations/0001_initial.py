# Generated by Django 3.1.2 on 2021-04-26 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staticInfo', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_time', models.DateTimeField()),
                ('available_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OfferAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('expire_time', models.DateTimeField()),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ManyToManyField(related_name='patient', through='appointment.OfferAppointment', to='user.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='provider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='user.provider'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='slot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staticInfo.weeklytimeslot'),
        ),
    ]
