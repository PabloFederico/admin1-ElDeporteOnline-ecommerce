from django.shortcuts import redirect
from django.views import View


class LandingPageView(View):

    def get(self, request):
        # TODO: remove when implementing landing page
        return redirect("full_catalog")
