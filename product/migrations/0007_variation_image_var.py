# Generated by Django 5.0.2 on 2024-03-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="variation",
            name="image_var",
            field=models.ImageField(
                blank=True, null=True, upload_to="produt_image_var/%Y/%m/"
            ),
        ),
    ]