from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default=None, null=False)
    phone = models.CharField(null=False, max_length=11, default=None)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
