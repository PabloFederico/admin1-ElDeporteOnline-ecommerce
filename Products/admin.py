from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_inline.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from Products.models import Product, ProductVariant, ProductVariantValue, ProductImage


# class ProductVariantValueInline(NestedTabularInline):
#     model = ProductVariantValue
#     extra = 1
#     fk_name = 'variant'
#
#
# class ProductVariantInline(NestedStackedInline):
#     model = ProductVariant
#     extra = 1
#     fk_name = 'product'
#     inlines = [ProductVariantValueInline]

class ProductImageInline(NestedStackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ["name", "short_description", "price", "image_preview"]
    search_fields = ['name']
    model = Product
    inlines = [ProductImageInline]
    # inlines = [ProductVariantInline]  # TODO: enable when product variants are implemented

    def image_preview(self, product):
        return mark_safe(f'<img src="{product.cover_image()}" width="100" height="100" />')


