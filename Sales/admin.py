from django.contrib import admin

# Register your models here.
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from Sales.models import Sale, Item


class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "total", "shipping_price", "address"]
    search_fields = ['name']
    readonly_fields = ['name', "date", "total", "shipping_price", 'address']
    model = Sale
    inlines = [ItemInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


