# Generated by Django 4.1.5 on 2023-06-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jalanidhiapp", "0011_complaints_replay_consumer_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaints_replay",
            name="category",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
