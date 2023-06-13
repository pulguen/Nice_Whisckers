from django.shortcuts import render
    from django.views.generic import TemplateView

# Create your views here.
class BarberiaView(TemplateView):
    template_name = "perfil_berberia.html"
    


class MiVista(TemplateView):
    template_name = 'mi_template.html'
