from django.db import models
from common.models import Customer


# Create your models here.
class CName(models.TextChoices):
    CBWAS = 'CBWAS', 'GOLF'
    BIGBRO = 'BIGBRO', 'COFFE'
    GONGNEWGI = 'GONGNEW', 'LOCAL PRODUCT'
    SCULFEE = 'SCULFEE', 'BIG SIZE WAER'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(choices=CName)


class Size(models.IntegerChoices):
    XS = 85, 'XS'
    X = 90, 'X'
    L = 95, 'L'
    XL = 100, 'XL'
    XXL = 105, 'XXL'
    XXXL = 110, 'XXXL'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    size = models.IntegerField(choices=Size.choices)
    date = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)

    img1 = models.URLField()
    img2 = models.URLField()
    img3 = models.URLField()
    img4 = models.URLField()
    img5 = models.URLField()


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
