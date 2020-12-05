from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from Products.models import Product
from Sales.models import Cart


class AddToCartView(View):

    def post(self, request):
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])

        product = get_object_or_404(Product, id=product_id)

        cart = Cart(request)
        cart.add_product(product, quantity)

        messages.success(request, 'Producto agregado al carrito!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
