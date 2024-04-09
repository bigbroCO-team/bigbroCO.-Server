from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='email address')
    phone_number = PhoneNumberField(
        unique=True,
        null=True,
        blank=True,
        verbose_name='phone number')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
