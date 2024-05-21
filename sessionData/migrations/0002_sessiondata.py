# Generated by Django 5.0.6 on 2024-05-20 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sessionData", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SessionData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.JSONField(verbose_name="Session Data")),
                ("type", models.CharField(max_length=100, verbose_name="Data Type")),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sessionData.usersession",
                        verbose_name="User Session",
                    ),
                ),
            ],
        ),
    ]
