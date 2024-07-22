from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.IntegerField(default=0)

    discount = models.FloatField(default=0)

    is_sale = models.BooleanField(default=False)

    open_stock = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    url = models.CharField(max_length=500)


class Option(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options'
    )

    name = models.CharField(max_length=100)

    stock = models.IntegerField()
