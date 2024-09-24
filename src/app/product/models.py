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

    discount = models.FloatField(default=0, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

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

    def __str__(self):
        return self.product.name


class Option(models.Model):

    STATUS = [
        ('on_sale', 'on_sale'),  # 판매중
        ('stop_sale', 'stop_sale'),  # 판매 중지
        ('sold_out', 'sold_out'),  # 품절
        ('discontinued', 'discontinued')  # 단종
    ]

    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options'
    )

    status = models.CharField(choices=STATUS, max_length=15, null=False, default='on_sale')

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
