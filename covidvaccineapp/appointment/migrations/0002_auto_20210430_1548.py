# Generated by Django 3.1.2 on 2021-04-30 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('expire_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ManyToManyField(related_name='patient', through='appointment.OfferAppointment', to='user.Patient'),
        ),
    ]
