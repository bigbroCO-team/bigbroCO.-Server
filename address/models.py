from django.db import models
from common.models import Customer
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    address = models.TextField()
    detail = models.TextField()
    phone = PhoneNumberField()
    request = models.TextField()

    def __str__(self):
        return self.customer.username