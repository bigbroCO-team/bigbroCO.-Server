import datetime

from django.db import models

from src.app.product.models import Product, Option
from src.app.user.models import User


# Create your models here.
class Order(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    """
    Order - Default field
    (delivery info, address)
    """
    name = models.CharField(max_length=100, default="<NAME>")
    tracking_number = models.CharField(max_length=30, null=True)
    delivery = models.CharField(max_length=30, null=True)
    total = models.IntegerField()
    address = models.CharField(max_length=50)
    address_detail = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    request = models.CharField(max_length=30)

    """
    Order - Payment field
    """
    # Default
    payment_key = models.CharField(max_length=200, null=True)
    order_id = models.CharField(max_length=64, null=True)
    total_amount = models.IntegerField(null=True)

    """
    Order - Metadata
    """
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')

    option = models.ForeignKey(Option, on_delete=models.PROTECT, related_name='items')

    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return self.product.name
