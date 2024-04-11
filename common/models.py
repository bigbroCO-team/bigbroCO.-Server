from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomerManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("User must have username")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Customer(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=300, null=False)
    phone_number = PhoneNumberField(unique=True, null=True)
