from django.urls import path

from LandingPage.views.landing_page_view import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
]
