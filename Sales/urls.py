from django.urls import path

from . import views

urlpatterns = [
    path('add-to-cart/', views.producto, name='add_to_cart'),
]