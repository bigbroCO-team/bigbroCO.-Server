from django.db import models
from common.models import Customer
from product.models import Product


# Create your models here.
class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
