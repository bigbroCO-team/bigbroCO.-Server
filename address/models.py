from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from common.models import Customer


# Create your models here.
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