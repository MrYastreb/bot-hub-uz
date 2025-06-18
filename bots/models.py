from django.db import models
from django.contrib.auth import get_user_model

# Получаем кастомную модель пользователя
User = get_user_model()


# Модель TestModel — для тестирования базы данных и миграций
class TestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Модель Bot — бот, принадлежащий пользователю
class Bot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bots')
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    webhook_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Модель Scenario — сценарий диалога бота с пользователем
class Scenario(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='scenarios')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Модель Block — блоки сценария общения бота с пользователем
class Block(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='blocks')
    title = models.CharField(max_length=255)
    message_text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# Модель Button — кнопки внутри блоков, привязанные к действиям
class Button(models.Model):
    ACTION_CHOICES = [
        ('go_to_block', 'Переход к другому блоку'),
        ('open_payment', 'Открытие формы оплаты'),
        ('external_link', 'Внешняя ссылка'),
    ]

    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='buttons')
    text = models.CharField(max_length=255)
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    target_block = models.ForeignKey(
        Block,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='target_buttons'
    )
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.block} → {self.text}"