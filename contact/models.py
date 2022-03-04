# util
import uuid

# 3rd-party
from phonenumber_field.modelfields import PhoneNumberField

# django
from django.db import models


class Contact(models.Model):
    """
        Contacts DB model
    """
    uid = models.CharField(
        unique=True,
        default=uuid.uuid1,
        max_length=50,
        primary_key=True,
    )
    user = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.CASCADE,
        related_name='contact',
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        null=True,
        blank=True,
        error_messages={"unique": "A contact with this phone number already exists"},
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
            Meta class of contacts model
        """
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.uid}'
