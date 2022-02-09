from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

USERTYPE = [
    (
        "buyer",
        "Buyer",
    ),
    (
        "seller",
        "Seller",
    ),
]


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField("email address", unique=True)
    native_name = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=10)
    purpose = models.CharField(max_length=100, choices=USERTYPE)
    orders = models.JSONField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "purpose", "phone_no"]

    def __str__(self):
        return "{}".format(self.email)
