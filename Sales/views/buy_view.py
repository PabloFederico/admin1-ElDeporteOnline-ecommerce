from django.shortcuts import render
from django.views import View


class BuyView(View):

    def get(self, request):
        return render(request, 'sales/buy.html')

    def post(self, request):
        # aca hay que recibir la compra y guardarla en la db
        # tambien hay que vaciar el carrito
        pass
