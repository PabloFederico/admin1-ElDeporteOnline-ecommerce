from django.urls import path

from . import views
from .views import RatingView

urlpatterns = [
    path('<int:producto_id>/', views.producto, name='producto'),
    path('rating/', RatingView.as_view(), name='rating'),
]