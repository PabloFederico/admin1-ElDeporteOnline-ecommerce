from django.urls import path

from . import views

urlpatterns = [
    path('agregar-al-carrito', views.producto, name='add_to_cart'),
]