from django.db import models
from phonenumbers.unicode_util import Category


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE),

    name = models.CharField(max_length=100),
    content = models.TextField(),
    price = models.DecimalField(max_digits=10, decimal_places=0),
    sale = models.DecimalField(max_digits=10, decimal_places=0),
    rdate = models.DateField(auto_now=False, auto_now_add=False),
    cnt = models.IntegerField(default=0),
    delete = models.BooleanField(default=False),


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
