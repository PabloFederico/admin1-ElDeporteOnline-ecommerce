from django.contrib import admin

# Register your models here.
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from Sales.models import Sale, Item


class ItemInline(NestedStackedInline):
    model = Item
    extra = 1


@admin.register(Sale)
class SaleAdmin(NestedModelAdmin):
    list_display = ["date"]
    search_fields = ['date']
    model = Sale
    inlines = [ItemInline]


