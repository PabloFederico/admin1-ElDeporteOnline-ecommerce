from django.shortcuts import render, redirect
from django.views import View

from Sales.models import Cart, Sale, Item, ItemVariant, SalePayment


class BuyView(View):

    def get(self, request):
        cart = Cart(request)
        if cart.count() == 0:
            return redirect("full_catalog")

        return render(request, 'sales/buy.html')

    def post(self, request):
        cart = Cart(request)

        if cart.count() == 0:
            return redirect("full_catalog")

        shipping_price = cart.get_total()["totalEnvio"]
        sale = Sale.objects.create(shipping_price=shipping_price, name=request.POST.get("name"),
                                   address=request.POST.get("address"))

        for entry in cart.get_products():
            product = entry.get('product')
            item = Item.objects.create(sale=sale, product=product, quantity=entry.get('quantity'),
                                       product_name=product.name, price=product.sale_price())
            for variant in entry["variants"]:
                ItemVariant.objects.create(item=item, variant=variant, variant_name=str(variant))

        payment_type = request.POST.get("payment")
        if payment_type == 'cash':
            SalePayment.objects.create(payment_type=payment_type, sale=sale)
        else:
            card = request.POST.get("cardNumber")
            expiry = request.POST.get("expiry")
            cvc = request.POST.get("cvc")
            SalePayment.objects.create(payment_type=payment_type, sale=sale, card=card, expiry=expiry, cvc=cvc)

        cart.clear()
        return render(request, 'sales/buy-complete.html')
