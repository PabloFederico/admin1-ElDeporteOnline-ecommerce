from django.contrib import admin

from Products.models import Product, ProductVariant, ProductVariantValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description", "price", "hide_from_catalog"]
    search_fields = ['name']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ["name", "product"]
    search_fields = ['name', 'product__name']


@admin.register(ProductVariantValue)
class ProductVariantValueAdmin(admin.ModelAdmin):
    list_display = ["name", "variant"]
    search_fields = ['name', 'variant__name']
