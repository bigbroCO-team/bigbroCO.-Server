from django.db import models
import uuid
from address.models import Address
from common.models import Customer
from product.models import Product


# Create your models here.
class Status(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'
    RETURNED = 'RETURNED', 'Returned'
    REFUNDED = 'REFUNDED', 'Refunded'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_DEFAULT, default="Anonymous")
    product = models.ManyToManyField(Product)
    address = models.ForeignKey(Address, on_delete=models.SET_DEFAULT, default="Deleted address")

    price = models.IntegerField(default=0)
    status = models.TextField(choices=Status)
    items = models.IntegerField(default=0)
