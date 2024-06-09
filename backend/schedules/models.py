from django.db import models
from users.models import CustomUser


class Schedule(models.Model):
    """Модель графика."""
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='schedules',
        verbose_name='Автор'
    )
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='Дата последнего обновления'
    )

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'

    def __str__(self):
        return self.title


class Work(models.Model):
    """Модель работы."""
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name='works'
    )
    name = models.CharField(max_length=200, verbose_name='Вид работ')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    resource_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Наименование ресурса'
    )
    resource_quantity = models.FloatField(verbose_name='Количество ресурса')
    resource_unit = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Единицы измерения'
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name
