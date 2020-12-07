from django.shortcuts import render
from django.views import View

from Products.models import Product
from Sales.models import Cart, Sale, Item


class BuyView(View):

    def get(self, request):
        return render(request, 'sales/buy.html')

    def post(self, request):
        # aca hay que recibir la compra y guardarla en la db
        # tambien hay que vaciar el carrito
        cart = Cart(request)
        items = []
        sale = Sale.objects.create()
        for entry in cart.get_products():
            product = Product.objects.get(pk=entry.get('product').id)
            item = Item.objects.create(sale=sale,product=product, quantity=entry.get('quantity'))
            items.append(item)

        sale.items.set(items)

        # sale.save()
        cart.clear()
        return render(request, 'sales/buy-complete.html')
