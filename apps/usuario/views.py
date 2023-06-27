from audioop import reverse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from apps.my_site.models import Persona
from apps.propietario.models import Propietario
from apps.turno.models import Turno
from apps.usuario.forms import CustomUserCreationForm
from apps.usuario.models import CustomUser
from apps.barberia.models import Barberia
# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil_usuario.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = CustomUser.objects.get(username=self.request.user.username)
        if usuario.es_propietario:
            try:
                propietario = Propietario.objects.get(propietario=self.request.user)
                barberia = propietario.barberia
                barberia_id = propietario.barberia.id
                turnos= Turno.objects.filter(usuario=self.request.user)
                context['propietario'] = propietario
                context['barberia'] = barberia
                context['barberia_id'] = barberia_id
                context['turno'] = list(turnos)
            except Propietario.DoesNotExist:
                # El usuario no es propietario
                pass
        
        return context
    

    