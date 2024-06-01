from django.db import models
from common.models import Customer


# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=False)
    zipcode = models.IntegerField(null=False)
    address = models.TextField(null=False)
    detail = models.TextField(null=False)
    request = models.TextField(null=False)
