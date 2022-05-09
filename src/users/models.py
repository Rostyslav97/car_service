from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, username=None, password=None, **kwargs):
        if not phone_number:
            raise ValueError("Phone number is required")
        if not password:
            raise ValueError("Password is required")
       
        phone_number = self.model(phone_number=phone_number)
        user = self.model(phone_number=phone_number, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, username=None, password=None, **kwargs):
        superuser_payload = {
            "phone_number": phone_number,
            "username": username,
            "password": password,
            "is_superuser": True, 
            "is_staff": True, 
            "is_active": True,
        }
        return self.create_user(**superuser_payload)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""

    phone_number = models.CharField(null=True, max_length=30, blank=True, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    car = models.CharField(max_length=50, null=True, blank=True, default=None)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_username(self):
        return self.phone_number