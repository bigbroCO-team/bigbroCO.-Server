from django.db import models

from src.app.client.user.models import User


class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    detail = models.CharField(max_length=30)

    def __str__(self):
        return self.address
