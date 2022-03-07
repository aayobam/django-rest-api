from uuid import uuid4
from django.db import models
from apps.authentication.manager import CustomUserManager
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=11)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD= 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()

    def get_name(self) -> str:
        return self.get_full_name()
