from django.contrib import admin
from . import models


class Variationline(admin.TabularInline):
    model = models.Variation
    extra = 1



class VariationAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'preco', 'preco_promotional', 'estoque')
    list_filter = ('product', 'name')
    search_fields = ('name', 'product__name')

class VariationImageAdmin(admin.ModelAdmin):
    list_display = ['image_var']








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
    inlines = [Variationline, ProductTableLineInline]




admin.site.register(models.VariationImage, VariationImageAdmin)
admin.site.register(models.Variation, VariationAdmin)
admin.site.register(models.ProductTabell)
admin.site.register(models.Product, ProdutoAdmin)

