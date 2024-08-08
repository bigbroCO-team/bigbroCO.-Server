from django.db import models

from user.models import User


# Create your models here.
class Address(models.Model):

    id = models.AutoField(
        primary_key=True,
        editable=False,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )

    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=10, default="<NAME>")
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    detail = models.CharField(max_length=30)
