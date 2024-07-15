from django.db import models

from user.models import User


# Create your models here.
class Address(models.Model):

    id = models.AutoField(
        primary_key=True,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    tag = models.CharField(max_length=10)
    zipcode = models.IntegerField(max_length=5)
    address = models.CharField(max_length=50)
    detail = models.CharField(max_length=30)
    request = models.CharField(max_length=255)
