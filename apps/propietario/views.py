from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from apps.barberia.models import Barberia
from apps.propietario.models import Propietario
from apps.post.models import Post

class AdminBarberView(LoginRequiredMixin, TemplateView):
    template_name = 'index_propietario.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        barberia_id = kwargs['id']
        barberia = get_object_or_404(Barberia, id=barberia_id)
        propietario = get_object_or_404(Propietario, barberia=barberia, propietario=self.request.user)
        posts = Post.objects.filter(propietario=propietario).order_by('-fecha_publicacion')
        context['barberia'] = barberia
        context['posts'] = posts
        return context