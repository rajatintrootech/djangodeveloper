from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CONDITION_CHOICES = [
    (
        "poor",
        "Poor",
    ),
    (
        "fair",
        "Fair",
    ),
    (
        "good",
        "Good",
    ),
    (
        "excellent",
        "Excellent",
    ),
]


class CarModel(models.Model):
    make = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    year = models.DateField()
    condition = models.CharField(max_length=1000, choices=CONDITION_CHOICES)
    asking_price = models.IntegerField(
        validators=[MaxValueValidator(100000), MinValueValidator(1000)]
    )
    sold = models.BooleanField(default=False)
    Seller_Info = models.ForeignKey(User, on_delete=models.CASCADE)
