from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Добавьте это для избежания конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username