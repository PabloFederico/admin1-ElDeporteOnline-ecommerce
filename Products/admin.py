from django.contrib import admin
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

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description", "price"]
    search_fields = ['name']
    model = Product
    inlines = [ProductImageInline]
    # inlines = [ProductVariantInline]  # TODO: enable when product variants are implemented


