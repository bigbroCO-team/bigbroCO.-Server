from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='<EMAIL>')
