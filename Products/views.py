from django.shortcuts import render

from .models import Product, ProductImage


def producto(request,producto_id):
    theproduct = Product.objects.get(pk=producto_id)
    return render(request, 'products/detail.html', {'theproduct': theproduct})
