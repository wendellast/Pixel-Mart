# Generated by Django 5.0.2 on 2024-03-17 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_remove_variation_image_var_variationimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="variationimage",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variation_images",
                to="product.product",
            ),
        ),
        migrations.AlterField(
            model_name="variationimage",
            name="image_var",
            field=models.ImageField(
                blank=True, null=True, upload_to="product_image_var/%Y/%m/"
            ),
        ),
    ]