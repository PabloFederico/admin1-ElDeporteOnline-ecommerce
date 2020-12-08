from django.shortcuts import render
from django.views import View

from Sales.models import Cart, Sale, Item


class BuyView(View):

    def get(self, request):
        return render(request, 'sales/buy.html')

    def post(self, request):
        cart = Cart(request)
        items = []

        shipping_price = cart.get_total()["totalEnvio"]
        sale = Sale.objects.create(shipping_price=shipping_price, name=request.POST.get("name"),
                                   address=request.POST.get("address"))

        for entry in cart.get_products():
            product = entry.get('product')
            item = Item.objects.create(sale=sale, product=product, quantity=entry.get('quantity'),
                                       product_name=product.name, price=product.sale_price())
            items.append(item)

        sale.items.set(items)

        cart.clear()
        return render(request, 'sales/buy-complete.html')
