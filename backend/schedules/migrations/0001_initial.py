# Generated by Django 5.0.6 on 2024-06-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
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
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "last_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего обновления"
                    ),
                ),
            ],
            options={
                "verbose_name": "График",
                "verbose_name_plural": "Графики",
            },
        ),
        migrations.CreateModel(
            name="Work",
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
                ("name", models.CharField(max_length=200, verbose_name="Вид работ")),
                ("start_date", models.DateField(verbose_name="Дата начала")),
                ("end_date", models.DateField(verbose_name="Дата окончания")),
                (
                    "resource_name",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Наименование ресурса",
                    ),
                ),
                (
                    "resource_quantity",
                    models.FloatField(verbose_name="Количество ресурса"),
                ),
                (
                    "resource_unit",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Единицы измерения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Работа",
                "verbose_name_plural": "Работы",
            },
        ),
    ]
