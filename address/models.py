import uuid

from django.db import models
from common.models import Customer


# Create your models here.
class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=False)
    zipcode = models.IntegerField(null=False)
    address = models.TextField(null=False)
    detail = models.TextField(null=False)
    request = models.TextField(null=False)
