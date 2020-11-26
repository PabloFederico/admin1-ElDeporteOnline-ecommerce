from django.urls import path

from . import views

urlpatterns = [
    path('<int:producto_id>/', views.producto, name='producto'),
]