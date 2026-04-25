from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

TITLE_LENGTH = 256
STATUS_LENGTH = PRIORITY_LENGTH = 20

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В процессе'
        DONE = 'done', 'Выполнена'

    class Priority(models.TextChoices):
        LOW = 'low', 'Низкий'
        MEDIUM = 'medium', 'Средний'
        HIGH = 'high', 'Высокий'

    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    status = models.CharField(
        max_length=STATUS_LENGTH,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name='Статус'
    )
    priority = models.CharField(
        max_length=PRIORITY_LENGTH,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name='Приоритет'
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дедлайн'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
