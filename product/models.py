from django.db import models
from common.models import Customer

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=False)




class Category(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=False)


class wishlist(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)