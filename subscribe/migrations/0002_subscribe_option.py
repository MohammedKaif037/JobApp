# Generated by Django 4.2.11 on 2024-05-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscribe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscribe",
            name="option",
            field=models.CharField(
                choices=[("W", "weekly"), ("M", "monthly")], default="W", max_length=2
            ),
            preserve_default=False,
        ),
    ]
