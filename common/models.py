from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='<EMAIL>')


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=False)
    zipcode = models.IntegerField(null=False)
    address = models.TextField(null=False)
    detail = models.TextField(null=False)
    phone = PhoneNumberField(null=False)
    request = models.TextField(null=False)

    def __str__(self):
        return self.customer.username