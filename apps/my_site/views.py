from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, CreateView):
    def get(self, request):
        context = {
            #"page_heading": "Nice Whisckers",
            "request": request  # Utiliza la misma clave "request" en el contexto
        }
        return render(request, 'core/home.html', {'user': request.user})
    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
    
    
    
    
    