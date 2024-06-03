from django.db import models
from common.models import Customer
from config.settings import DEFAULT_IMAGE_URL


# Create your models here.
class Product(models.Model):
    class Category(models.TextChoices):
        CBWAS = 'CBWAS'
        BIGBRO = 'BIGBRO'
        GONGNEWGI = 'GONGNEWGI'
        SCULFEE = 'SCULFEE'

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    category = models.TextField(choices=Category.choices)
    date = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField(default=DEFAULT_IMAGE_URL, null=False)


class Value(models.IntegerChoices):
    ONE = 1, 'ONE'
    TWO = 2, 'TWO'
    THREE = 3, 'THREE'
    FOUR = 4, 'FOUR'
    FIVE = 5, 'FIVE'


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    value = models.IntegerField(choices=Value.choices)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = (('product', 'user'),)
