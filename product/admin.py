from django.contrib import admin
from . import models


class Variationline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["name", 'description_short',
                    'price_marketing', 'price_marketing_promotional']
    inlines = [Variationline]


admin.site.register(models.Product, ProdutoAdmin)
admin.site.register(models.Variation)
