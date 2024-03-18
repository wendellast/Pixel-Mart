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


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description_short",
        "price_marketing",
        "price_marketing_promotional",
    ]
    inlines = [Variationline, ProductImagesLine, ProductTableLineInline]


admin.site.register(models.ProductTabell)
admin.site.register(models.Variation)
admin.site.register(models.Product, ProdutoAdmin)
