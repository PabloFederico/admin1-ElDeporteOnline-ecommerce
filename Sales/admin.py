from django.contrib import admin

from Sales.models import Sale, Item


# Register your models here.


class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

    fields = ('product_name', 'quantity', 'price', 'variantes')
    readonly_fields = ('product_name', 'quantity', 'price', 'variantes')

    def variantes(self, item):
        data = [variant.variant_name for variant in item.variants.all()]
        return "\n".join(data)


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


