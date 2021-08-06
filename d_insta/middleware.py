"""d-insta middleware Catalog."""

# Django
from typing import Reversible
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware():
    """Profile completion middleware

    Ensures every user that is interacting with the platform
    have their picture and biograpy filled
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture and not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
