from django.db import models

from src.app.client.product.models import Product, Option
from src.app.client.user.models import User


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
        )

    def __str__(self):
        return f"{self.user} : {self.product}"


    def increase_count(self):
        self.count += 1
        self.save()
        return self