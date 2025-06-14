from django.db import models
from users.models import User

class Bot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    webhook_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


class Block(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message_text = models.TextField()
    order = models.PositiveIntegerField(default=0)


class Button(models.Model):
    ACTION_CHOICES = [
        ('go_to_block', 'Перейти к блоку'),
        ('open_payment', 'Открыть оплату'),
        ('external_link', 'Внешняя ссылка')
    ]

    block = models.ForeignKey(Block, related_name='buttons', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    target_block = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.block} → {self.text}"