import uuid
from django.db import models
from common.models import Customer
from config.settings import DEFAULT_IMAGE_URL


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    url = models.URLField(max_length=500, unique=False, default=DEFAULT_IMAGE_URL)
