from django.db import models
from common.models import Customer


# Create your models here.
class CName(models.TextChoices):
    CBWAS = 'CBWAS'
    BIGBRO = 'BIGBRO'
    GONGNEWGI = 'GONGNEW'
    SCULFEE = 'SCULFEE'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(choices=CName)

    def __str__(self):
        return self.name


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
    size = models.IntegerField(choices=Size.choices, null=True)
    date = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)

    img1 = models.URLField(default='https://test-bigbro-bucket.s3.ap-northeast-2.amazonaws.com/images/161764121_342336863872451_1790344446721071304_n.jpg', null=False)
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
