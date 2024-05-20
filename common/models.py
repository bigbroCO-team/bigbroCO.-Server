from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='<EMAIL>')
    phone = models.CharField(null=False, max_length=11, default='<PHONE>')


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField(default='<URL>')
