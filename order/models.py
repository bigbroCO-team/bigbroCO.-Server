from django.db import models

from product.models import Product
from user.models import User


# Create your models here.
class Order(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    """
    Order - Default field
    (delivery info, address)
    """
    delivery = models.CharField(max_length=30)
    tracking_number = models.CharField(max_length=30)
    total = models.IntegerField()
    address = models.CharField(max_length=50)
    address_detail = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    request = models.CharField(max_length=30)

    """
    Order - Payment field
    """
    # Default
    payment_key = models.CharField(max_length=200)
    order_id = models.CharField(max_length=64)
    total_amount = models.IntegerField()

    """
    Order - Metadata
    """
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    order = models.ForeignKey(Order, on_delete=models.PROTECT)
