from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Product, ProductImage, ProductRating


def producto(request, producto_id):
    theproduct = Product.objects.get(pk=producto_id)
    return render(request, 'products/detail.html', {'theproduct': theproduct})


class RatingView(View):
    def post(self, request):

        if 'votados' not in request.session:
            request.session['votados'] = []
        votados = request.session['votados']

        producto_id = request.POST.get("product_id", "")
        if producto_id in votados:
            return HttpResponse("ya voto antes")

        value = request.POST.get("value", 0)
        theproduct = Product.objects.get(pk=producto_id)
        rating = ProductRating.objects.create(value=value, product=theproduct)

        votados = votados + [producto_id]
        request.session['votados'] = votados

        return HttpResponse(theproduct.ratings.values(), {'votados':votados})
        # return render(request, 'products/detail.html', {'theproduct': theproduct})

    def get(self, request):
        if 'votados' not in request.session:
            request.session['votados'] = []
        votados = request.session['votados']

        producto_id = request.GET.get("product_id", "")
        if producto_id in votados:
            return HttpResponse("readonly:true")
        else:
            return HttpResponse("readonly:false")
