# Imports sin from del sistema o de django.
import os
# Imports de django o librerias de terceros
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Imports de nuestras apps
from apps.barberia.forms import BarberiaForm
from apps.barberia.models import Barberia
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

# backendifts/alumno
class BarberiasView(LoginRequiredMixin, TemplateView):
    template_name = 'index_barberias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barberias'] = Barberia.objects.all()
        return context

# backendifts/alumno/<int: id>
class BarberiaView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil_barberia.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vamos a buscar al alumno que esta relacionado con quien inicia sesion
        barberia_id = kwargs['id']
        barberia = Barberia.objects.get(id=barberia_id, user=self.request.user)
        if not Barberia:
            pass
            # Redirect al inicio PAGINA_INICIO
            # return Response(401, {"data": "Este usuario no es tuyo, no se puede acceder."})
        context['Barberia'] = barberia
        return context

# Request a 127.0.0.1:8000/alumno/10
# Cuando recibilos el request si el alumno 10 esta relacionado con el usuario que inicio sesion continuamos
# Si no esta relacionado, redireccionamos a otra pagina y tiramos un error 401 No Autorizado
# Si nuestro usuario es el ID 5, relacionado con el alumno 8, solo podremos accedera a 127.0.0.1:8000/alumno/8
# No hace falta enviar el id de nuestro alumno, sino simplemente hacer una URL que se llame 127.0.0.1:8000/alumno
# Esa URL busca nuestro ID de alumno y nos devuelve unicamente nuestro objeto de alumno

class BarberiaFormView(LoginRequiredMixin, CreateView):
    form_class = BarberiaForm
    template_name = 'create_barberia.html'
    success_url = reverse_lazy('index_barberias')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)