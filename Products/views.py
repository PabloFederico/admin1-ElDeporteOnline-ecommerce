from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

def producto(request,producto_id):
    theproduct = Product.objects.get(pk=producto_id)
    return render(request, 'products/product_detail.html',{'theproduct':theproduct})