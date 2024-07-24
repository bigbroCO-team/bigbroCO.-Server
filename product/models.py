from django.db import models


# Create your models here.
class Product(models.Model):
    CATEGORY = [
        ('CBWAS', 'CBWAS'),
        ('SCB', 'S.C.B'),
        ('BIGBRO', 'BIGBRO'),
        ('GONGNEWGI', 'GONGNEWGI'),
        ('SCULFEE', 'SCULFEE')
    ]

    id = models.AutoField(primary_key=True)

    category = models.CharField(choices=CATEGORY, max_length=10, null=False)

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.IntegerField(default=0)

    discount = models.FloatField(default=0)

    on_sale = models.BooleanField(default=True)

    open_stock = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} : {self.name}"


class Image(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    url = models.CharField(max_length=500)

    def __str__(self):
        return self.product.name


class Option(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options'
    )

    name = models.CharField(max_length=100)

    stock = models.IntegerField()

    def __str__(self):
        return self.name
