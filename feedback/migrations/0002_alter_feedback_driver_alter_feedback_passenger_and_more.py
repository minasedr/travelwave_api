# Generated by Django 5.0.3 on 2024-03-16 05:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
        ("rides", "0002_alter_ride_options_alter_ridehistory_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="driver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passenger_feedbacks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="passenger",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rider_feedbacks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="ride",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rides.ride"
            ),
        ),
    ]
