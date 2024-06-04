import uuid

from django.db import models

from common.models import Customer
from product.models import Product


# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'customer'], name='unique_cart_product_and_customer'),
        ]


class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'customer'], name='unique_wishlist_product_and_customer'),
        ]