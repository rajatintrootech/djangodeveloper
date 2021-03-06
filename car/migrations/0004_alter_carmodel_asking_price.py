# Generated by Django 4.0.2 on 2022-02-09 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0003_alter_carmodel_asking_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmodel",
            name="asking_price",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(100000),
                    django.core.validators.MinValueValidator(1000),
                ]
            ),
        ),
    ]
