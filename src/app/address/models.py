from django.db import models

from src.app.user.models import User


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
    zipcode = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    detail = models.CharField(max_length=30)

    def __str__(self):
        return self.zipcode
