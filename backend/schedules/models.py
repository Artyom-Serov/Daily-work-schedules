from django.db import models
from users.models import CustomUser


class Schedule(models.Model):
    """Модель графика."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    last_modified = models.DateTimeField(auto_now=True)

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
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Модель ресурса."""
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return self.name


class WorkResource(models.Model):
    """Ресурсы для работ с количеством."""
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='quantity'
    )
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name='quantity'
    )
    quantity = models.FloatField()

    class Meta:
        verbose_name = 'Количество ресурса'
        verbose_name_plural = 'Количество ресурсов'

    def __str__(self):
        return f"{self.resource.name} for {self.work.name}"
