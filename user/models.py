# util
import uuid

# django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
        Custom User manager class
    """
    def create_user(self, email, secret_code, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, secret_code=secret_code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        Custom User DB model extended from Abstract django user class
        with custom registration and login functionality
    """
    uid = models.CharField(
        unique=True,
        default=uuid.uuid1,
        max_length=50,
        primary_key=True
    )
    email = models.EmailField(
        "email_address",
        unique=True,
        null=True,
        blank=True,
        error_messages={"unique": "A user with this email already exists"},)
    username = models.CharField(
        "username",
        max_length=255,
        unique=True,
        default=uuid.uuid1,
        error_messages={"unique": "A user with this username already exists"}
    )
    secret_code = models.CharField(
        "secret_code",
        max_length=255,
        default=uuid.uuid1,
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active",
    )
    is_staff = models.BooleanField(
        "staff_status",
        default=False,
        help_text="Designate whether the user can log into this admin site",
    )
    is_admin = models.BooleanField(
        "admin",
        default=False,
        help_text="Designate whether the user should be treated as admin",
    )
    date_joined = models.DateTimeField(
        "date joined",
        default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "secret_code",
    ]

    def get_short_name(self):
        return f"{self.username}"

    def has_perm(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
