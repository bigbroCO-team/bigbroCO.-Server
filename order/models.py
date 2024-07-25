from django.db import models

from product.models import Product


# Create your models here.
class Order(models.Model):
    pass


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)