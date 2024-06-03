import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(default=None, null=False)
    phone = models.CharField(max_length=11)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
