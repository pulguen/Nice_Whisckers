from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from apps.profesional.forms import ProfesionalForm
from apps.profesional.models import Profesional
from apps.propietario.models import Propietario

class ProfesionalCreateView(LoginRequiredMixin, CreateView):
    model=Profesional
    form_class = ProfesionalForm
    template_name = 'create_Profesional.html'
    success_url = reverse_lazy('home')
            
    def form_valid(self, form):
        propietario = get_object_or_404(Propietario, propietario=self.request.user)
        barberia = propietario.barberia.id
        form.instance.barberia_id = barberia
        return super().form_valid(form)