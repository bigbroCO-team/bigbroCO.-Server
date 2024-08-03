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

    tag = models.CharField(max_length=10, null=False)
    zipcode = models.IntegerField(null=False)
    phone = models.CharField(max_length=11, null=False, default="<PHONE>")
    address = models.CharField(max_length=50, null=False)
    detail = models.CharField(max_length=30, null=False)
    request = models.CharField(max_length=255, null=False)
