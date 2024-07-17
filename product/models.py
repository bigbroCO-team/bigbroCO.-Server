from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    description = models.TextField()

    open_stock = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
