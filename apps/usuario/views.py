from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.usuario.models import Usuario
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil_usuario.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = User.objects.get(username=self.request.user.username)
        if not Usuario:
            pass
            # Redirect al inicio PAGINA_INICIO
            # return Response(401, {"data": "Este usuario no es tuyo, no se puede acceder."})
        context['Usuario'] = usuario
        return context
