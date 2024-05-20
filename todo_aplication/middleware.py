from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path in [reverse('login'), reverse('sign-up')]:
                return redirect('home')  # Asegúrate de que 'home' es el nombre de tu vista de inicio
        response = self.get_response(request)
        return response
