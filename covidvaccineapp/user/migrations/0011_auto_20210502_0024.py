# Generated by Django 3.1.2 on 2021-05-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210502_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='max_distance_preferences',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
