from django.db import models

from product.models import Product


# Create your models here.
class Option(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options'
    )

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    discount = models.FloatField()

    stock = models.IntegerField()
