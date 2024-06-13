# Generated by Django 5.0.6 on 2024-06-12 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="work",
            name="resource_name",
        ),
        migrations.RemoveField(
            model_name="work",
            name="resource_quantity",
        ),
        migrations.RemoveField(
            model_name="work",
            name="resource_unit",
        ),
        migrations.AlterField(
            model_name="work",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Вид работ"),
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Наименование ресурса",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(verbose_name="Количество ресурса"),
                ),
                (
                    "unit",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Единицы измерения",
                    ),
                ),
                (
                    "work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resources",
                        to="schedules.work",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ресурс",
                "verbose_name_plural": "Ресурсы",
            },
        ),
    ]
