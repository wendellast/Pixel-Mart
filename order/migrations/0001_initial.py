# Generated by Django 5.0.2 on 2024-02-13 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("total", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Approved"),
                            ("C", "Criated"),
                            ("R", "Disapproved"),
                            ("P", "Pending"),
                            ("S", "Sent"),
                            ("F", "finished"),
                        ],
                        default="c",
                        max_length=1,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrdenItem",
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
                ("product", models.CharField(max_length=255)),
                ("product_id", models.PositiveIntegerField()),
                ("variation", models.CharField(max_length=255)),
                ("variation_id", models.PositiveIntegerField()),
                ("price", models.FloatField()),
                ("promotional_price", models.FloatField(default=0)),
                ("quantity", models.PositiveIntegerField()),
                ("imagem", models.CharField(max_length=2000)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
            ],
        ),
    ]
