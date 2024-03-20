from django.contrib import admin
from . import models


class Variationline(admin.TabularInline):
    model = models.Variation
    extra = 1

class ProductImagesLine(admin.TabularInline):
    model = models.ImagesProduct
    extra = 1

class ProductTableLineInline(admin.TabularInline):
    model = models.ProductTabell
    extra = 1

class VariationAdmin(admin.ModelAdmin):
    list_display = [
      "image_var"
    ]


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description_short",
        "price_marketing",
        "price_marketing_promotional",
    ]
    inlines = [Variationline, ProductImagesLine, ProductTableLineInline]


admin.site.register(models.Product, ProdutoAdmin)
admin.site.register(models.ProductTabell)
admin.site.register(models.Variation, VariationAdmin)
