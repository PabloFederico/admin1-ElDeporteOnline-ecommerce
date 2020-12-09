from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from Products.models import Product, ProductVariantValue
from Sales.models import Cart


class AddToCartView(View):

    def post(self, request):
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])

        product = get_object_or_404(Product, id=product_id)

        variants = []
        for variant in product.variants_with_values():
            variant_id = request.POST[f"variant_{variant.id}"]
            variant_value = get_object_or_404(ProductVariantValue, id=variant_id)
            variants.append(variant_value)

        cart = Cart(request)
        cart.add_product(product, quantity, variants)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RemoveFromCartView(View):

    def post(self, request):
        product_id = request.POST["product_id"]

        product = get_object_or_404(Product, id=product_id)

        cart = Cart(request)
        cart.remove_product(product)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
