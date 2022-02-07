import jwt
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager




username_validator = UnicodeUsernameValidator()

class MyUserManager(UserManager):

    # save users created
    def _create_user(self, username, email, password, **extra_fields):
        """
        creates and save a user with the given email, username and password
        """
        if not username:
            raise ValueError("Username is required")

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #creates regular user
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    # creates super user
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError("is_active should be set to True")

        if extra_fields.get('is_staff') is not True:
            raise ValueError("is_staff should be set to True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("is superuser should be set to True")
        
        return self._create_user(username, email, password, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), 
        max_length=50,
        unique=True, 
        validators=[username_validator], 
        help_text=_("must not be more than 50 alphanumeric values"), 
        error_messages={'unique':_('A user with that username already exists.')}
    )

    email = models.EmailField(
        _('email'),
        max_length=150,
        unique=True,
        blank=False,
        help_text=_("must not be more than 150 alphanumeric values"),
        error_messages={'unique':_('A user with that email already exists.')},
    )

    first_name = models.CharField(_('first_name'), max_length=100, blank=True)
    last_name = models.CharField(_('last_name'), max_length=100, blank=True)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    is_active = models.BooleanField(_('is_active'), default=False)
    is_staff = models.BooleanField(_('is_staff'),default=False)
    is_superuser = models.BooleanField(_('is_superuser'),default=False)
    email_verified = models.BooleanField(_('email_verified'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    @property
    def token(self):
        user_toke = jwt.decode({"email": self.email, "username": self.username,"exp": datetime.utcnow() + timedelta(hours=10)},
        settings.SECRET_KEY,
        algorithm="HS256",
        )
        return user_toke