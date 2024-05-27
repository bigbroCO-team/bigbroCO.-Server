from django.db import models
from common.models import Customer


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)

    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)

    img1 = models.URLField(default='DAC17638-6429-4172-9AB7-35F4313C2394_1_105_c-removebg-preview (2).png', null=False)
    img2 = models.URLField(default=None, null=True)
    img3 = models.URLField(default=None, null=True)
    img4 = models.URLField(default=None, null=True)
    img5 = models.URLField(default=None, null=True)


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
        return str(self.id) + self.user.username

    class Meta:
        unique_together = (('product', 'user'),)
