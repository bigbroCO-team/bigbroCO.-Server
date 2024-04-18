from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
