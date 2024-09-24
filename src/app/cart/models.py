from django.db import models

from src.app.product.models import Product, Option
from src.app.user.models import User


# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        null=False
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
        )

    def __str__(self):
        return self.user.username + " : " + self.product.name
