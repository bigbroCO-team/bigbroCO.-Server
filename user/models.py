from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(
        unique=True,
        null=False
    )

    signature = models.CharField(
        max_length=4,
        null=False
    )

    phone = models.CharField(
        max_length=12,
        null=False
    )

    def __str__(self):
        return self.email
