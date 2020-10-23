from django.urls import path

from Catalog.views.full_catalog_view import FullCatalogView

urlpatterns = [
    path('', FullCatalogView.as_view(), name='full_catalog'),
]