from django.db import models

from product.models import Product
from user.models import User


# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='carts',
    )

    def __str__(self):
        return self.user.username + " : " + self.product.name
