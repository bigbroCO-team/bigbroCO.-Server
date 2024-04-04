from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(AbstractUser):
    phone_number = PhoneNumberField(verbose_name="Phone Number")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.username
