from django.contrib import admin
from . import models


class Variationline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [Variationline]


admin.site.register(models.Product, ProdutoAdmin)
admin.site.register(models.Variation)
