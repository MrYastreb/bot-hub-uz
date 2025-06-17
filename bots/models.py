from django.db import models
from django.contrib.auth import get_user_model

# Получаем кастомную модель пользователя через AUTH_USER_MODEL
User = get_user_model()

class Block(models.Model):
    """
    Модель блока для конструктора ботов.
    Каждый блок связан с сценарием и содержит текст сообщения.
    """
    scenario = models.ForeignKey('Scenario', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message_text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Button(models.Model):
    """
    Модель кнопки для конструктора ботов.
    Кнопка связана с блоком и может иметь действие (например, переход к другому блоку или открытие формы оплаты).
    """
    ACTION_CHOICES = [
        ('go_to_block', 'Переход к другому блоку'),
        ('open_payment', 'Открытие формы оплаты'),
        ('external_link', 'Внешняя ссылка')
    ]

    block = models.ForeignKey(Block, related_name='buttons', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    target_block = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='target_buttons'
    )
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.block} → {self.text}"