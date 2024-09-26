from django.contrib.auth.models import AbstractUser
from django.db import (models)

# Create your models here.
class User(AbstractUser):

    username = models.CharField(max_length=30, null=True, unique=True)

    password = models.CharField(max_length=120, null=True)

    email = models.EmailField(unique=True)

    signature = models.CharField(max_length=4)

    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.email
