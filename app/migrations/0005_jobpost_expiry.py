# Generated by Django 4.2.11 on 2024-04-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_jobpost_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="expiry",
            field=models.DateField(null=True),
        ),
    ]
