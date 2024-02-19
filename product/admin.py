from django.contrib import admin
from . import models




class Variationline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description_short",
        "price_marketing",
        "price_marketing_promotional",
    ]
    inlines = [Variationline]


class ImagemBannerInline(admin.TabularInline):
    model = models.ImagemBanner.banners.through
    extra = 1

class BannerAdmin(admin.ModelAdmin):
    inlines = [ImagemBannerInline]


admin.site.register(models.Product, ProdutoAdmin)
admin.site.register(models.Banner, BannerAdmin)
admin.site.register(models.ImagemBanner)
admin.site.register(models.Variation)
