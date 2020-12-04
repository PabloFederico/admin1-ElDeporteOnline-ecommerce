from django.urls import path

from .views.cart_view import AddToCartView

urlpatterns = [
    path('agregar-al-carrito', AddToCartView.as_view(), name='add_to_cart'),
]
