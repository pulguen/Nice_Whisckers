from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, ListView, TemplateView, DetailView
from apps import turno
from apps.barberia.models import Barberia
from apps.profesional.models import Profesional
from apps.turno.models import Turno
from apps.turno.forms import ConfirmarTurnoForm, ElegirBarberiaForm, ElegirProfesionalForm, NuevoTurnoForm

class NuevoTurnoView(LoginRequiredMixin, FormView):
    template_name = 'nuevo_turno.html'
    form_class = NuevoTurnoForm
    
    def form_valid(self, form):
        self.request.session['dia'] = form.cleaned_data['dia']
        self.request.session['hora'] = form.cleaned_data['hora']
        return redirect('turno:elegir_barberia')

class ElegirBarberiaView(LoginRequiredMixin, View):
    def get(self, request):
        form = ElegirBarberiaForm()
        dia = self.request.session.get('dia')
        hora = self.request.session.get('hora')
        context = {
            'form': form,
            'dia': dia,
            'hora': hora
        }
        return render(request, 'elegir_barberia.html', context)

    def post(self, request):
        form = ElegirBarberiaForm(request.POST)
        if form.is_valid():
            barberia_id = form.cleaned_data['barberia'].id
            self.request.session['barberia_id'] = barberia_id
            return redirect('turno:elegir_profesional')
        else:
            context = {'form': form}
            return render(request, 'elegir_barberia.html', context)

class ElegirProfesionalView(LoginRequiredMixin, ListView):
    def get(self, request):
        barberia_id = self.request.session.get('barberia_id')
        if barberia_id:
            dia = self.request.session.get('dia')
            hora = self.request.session.get('hora')
            barberia = Barberia.objects.get(id=barberia_id)
            profesionales = Profesional.objects.filter(barberia=barberia)
            form = ElegirProfesionalForm(barberia=barberia)
            context = {
                'dia': dia,
                'hora': hora,
                'profesionales': profesionales,
                'barberia': barberia,
                'form': form,
            }
            return render(request, 'elegir_profesional.html', context)
        else:
            return redirect('turno:elegir_barberia', barberia_id=barberia_id)
        
    def post(self, request):
        barberia_id = self.request.session.get('barberia_id')
        barberia = Barberia.objects.get(id=barberia_id)
        form = ElegirProfesionalForm(request.POST,barberia=barberia)
        if form.is_valid():
            profesional = form.cleaned_data['profesional']           
            profesional_id = profesional.id
            self.request.session['profesional_id'] = profesional_id  # Guardar el ID del profesional en la sesión
            dia = self.request.session.get('dia')
            hora = self.request.session.get('hora')
            barberia_id = barberia_id
            profesional_id = self.request.session.get('profesional_id')
            if dia and hora and barberia_id and profesional_id:
                return redirect('turno:confirmar_turno')
        else:
            barberia_id = self.request.session.get('barberia_id')
            dia = self.request.session.get('dia')
            hora = self.request.session.get('hora')
            barberia = Barberia.objects.get(id=barberia_id)
            profesionales = Profesional.objects.filter(barberia=barberia)
            form = ElegirProfesionalForm(barberia=barberia)
            context = {
                'dia': dia,
                'hora': hora,
                'profesionales': profesionales,
                'barberia': barberia,
                'form': form,
            }
            return render(request, 'elegir_profesional.html', context)

class ConfirmarTurnoView(LoginRequiredMixin, DetailView):  
    def get(self, request):
        profesional_id = self.request.session.get('profesional_id')
        if profesional_id:            
            dia = self.request.session.get('dia')
            hora = self.request.session.get('hora')
            barberia_id = self.request.session.get('barberia_id')
            profesional_id = self.request.session.get('profesional_id')
        try:
            barberia = Barberia.objects.get(id=barberia_id)
        except Barberia.DoesNotExist:
            # Manejar el caso en que no se encuentre la barbería
            # Puedes redirigir a una página de error o realizar alguna otra acción
            return HttpResponse('Barbería no encontrada')
        try:
            profesional = Profesional.objects.get(id=profesional_id)
        except Profesional.DoesNotExist:
            # Manejar el caso en que no se encuentre el profesional
            # Puedes redirigir a una página de error o realizar alguna otra acción
            return HttpResponse('Profesional no encontrado')
        barberia_choices = [(barberia.id, barberia.nombre)]
        profesional_choices = [(profesional.id, profesional.nombre)]
        form = ConfirmarTurnoForm(
            barberia_choices=barberia_choices,
            profesional_choices=profesional_choices,
            initial={
                'dia': dia,
                'hora': hora,
                'barberia': barberia_id,
                'profesional': profesional_id,
            },
        )
        
        context = {
            'form': form,
            'dia': dia,
            'hora': hora,
            'barberia': barberia.nombre,
            'profesional': profesional.nombre,
        }

        return render(request, 'confirmar_turno.html', context)

    def post(self, request):
        dia = request.session.get('dia')
        hora = request.session.get('hora')
        usuario = self.request.user        
        barberia_id = request.session.get('barberia_id')
        profesional_id = request.session.get('profesional_id')
        if dia and hora and barberia_id and profesional_id:
            turno = Turno(
                barberia_id=barberia_id,
                profesional_id=profesional_id,
                usuario=usuario,
                dia=dia,
                hora=hora,
            )
            turno.save()
            self.request.session['turno_id'] = turno.id
            del self.request.session['dia']
            del self.request.session['hora']
            del self.request.session['barberia_id']
            del self.request.session['profesional_id']
            return redirect('turno:confirmacion_turno')
        else:
            return redirect('turno:confirmar_turno')

class ConfirmacionTurnoView(LoginRequiredMixin,TemplateView):
    template_name = 'confirmacion_turno.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        turno_id = self.request.session.get('turno_id')
        turno = get_object_or_404(Turno, id=turno_id)
        context['turno'] = turno
        return context