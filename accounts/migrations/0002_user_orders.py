# Generated by Django 4.0.2 on 2022-02-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="orders",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
