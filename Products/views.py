from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, ProductImage

def producto(request,producto_id):
    theproduct = Product.objects.get(pk=producto_id)
    fotos = ProductImage.objectsProductsImages.filter(product = theproduct)  
    return render(request, 'products/detail.html',{'theproduct':theproduct,'fotos':fotos})