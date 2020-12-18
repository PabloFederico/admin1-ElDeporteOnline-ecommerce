from django.views.generic import ListView

from Products.models import Product


class FullCatalogView(ListView):
    model = Product
    template_name = "catalog/full_catalog.html"

    def get_queryset(self):
        price_order = self.request.GET.get("orden_precio", "")
        filtro = self.request.GET.get("filtro", "")
        return Product.objects.for_catalog().order_by_price(price_order).filter_by_text(filtro)

    def get_context_data(self, **kwargs):
        context = super(FullCatalogView, self).get_context_data(**kwargs)
        context['price_order'] = self.request.GET.get("orden_precio", "")
        context['filter'] = self.request.GET.get("filtro", "")
        return context
