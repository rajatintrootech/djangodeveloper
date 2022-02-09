# Generated by Django 4.0.2 on 2022-02-09 21:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0002_alter_carmodel_condition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmodel",
            name="asking_price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[
                    django.core.validators.MaxValueValidator(100000),
                    django.core.validators.MinValueValidator(1000),
                ],
            ),
        ),
    ]
