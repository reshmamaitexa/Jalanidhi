# Generated by Django 4.1.5 on 2023-05-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("jalanidhiapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="panchayath_details",
            name="meter_reader",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="jalanidhiapp.meter_reader",
            ),
            preserve_default=False,
        ),
    ]
