from django.db import models

from address.models import Address
from common.models import Customer
from product.models import Product


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    status = models.TextField()
    items = models.IntegerField(default=0)
