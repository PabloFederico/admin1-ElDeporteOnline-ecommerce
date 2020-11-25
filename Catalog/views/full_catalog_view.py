from django.views.generic import ListView

from Products.models import Product


class FullCatalogView(ListView):
    model = Product
    template_name = "catalog/full_catalog.html"

    def get_queryset(self):
        return Product.objects.for_catalog()
