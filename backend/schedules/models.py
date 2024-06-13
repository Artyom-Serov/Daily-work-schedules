from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()
        if not self.pk:
            return
        if not self.works.exists():
            raise ValidationError(
                'В графике должна быть хотя бы одна работа.'
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Work(models.Model):
    """Модель работы."""
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name='works'
    )
    name = models.CharField(max_length=150, verbose_name='Вид работ')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def clean(self):
        super().clean()
        if not self.start_date or not self.end_date:
            raise ValidationError(
                'Указание дат начала и окончания работ обязательно.'
            )
        if self.end_date < self.start_date:
            raise ValidationError(
                'Дата окончания не может быть раньше даты начала.'
            )

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Модель ресурса."""
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='resources'
    )
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Наименование ресурса'
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество ресурса')
    unit = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Единицы измерения'
    )

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def clean(self):
        super().clean()
        if self.quantity is None or self.unit is None or self.unit == '':
            raise ValidationError(
                'Количество и единица измерения не могут быть пустыми'
            )
        if self.quantity < 0:
            raise ValidationError(
                'Количество ресурса не может быть отрицательным числом'
            )

    def __str__(self):
        return f"{self.name} {self.quantity} {self.unit}"
