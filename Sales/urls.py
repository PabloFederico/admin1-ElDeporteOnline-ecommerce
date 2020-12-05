from django.urls import path

from .views.cart_view import AddToCartView, RemoveFromCartView

urlpatterns = [
    path('agregar-al-carrito', AddToCartView.as_view(), name='add_to_cart'),
    path('sacar-del-carrito', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
