from django.db import models
from django.conf import settings
from PIL import Image
import os
from django.utils.text import slugify
import random
from utils import tools


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description_short = models.TextField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(upload_to="produt_image/%Y/%m/", blank=False, null=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    price_marketing = models.FloatField()
    price_marketing_promotional = models.FloatField(default=0)
    type_variation = models.CharField(
        default="v",
        max_length=1,
        choices=(
            ("V", "Variavel"),
            ("S", "Simples"),
        ),
    )

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}-{round(random.uniform(0, 10000), 3)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def parce(self):
        if self.price_marketing_promotional:
            return f'{round(self.price_marketing_promotional / 12, 2)}'

        return f'{round(self.price_marketing / 12, 2)}'



    def __str__(self):
        return self.name



class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promotional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def _str__(self):
        return self.name or self.product.name
