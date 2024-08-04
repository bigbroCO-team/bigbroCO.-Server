from django.db import models

from product.models import Product, Option
from user.models import User


# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='carts',
    )

    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE,
        related_name='options',
    )

    count = models.IntegerField(default=1)

    class Meta:
        unique_together = (
            ('user', 'option'),
            ('product', 'option')
        )

    def __str__(self):
        return self.user.username + " : " + self.product.name
