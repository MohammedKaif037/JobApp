# Generated by Django 4.2.11 on 2024-04-26 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_jobpost_expiry"),
    ]

    operations = [
        migrations.CreateModel(
            name="location",
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
                ("street", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("zip", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="jobpost",
            name="location",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.location",
            ),
        ),
    ]
