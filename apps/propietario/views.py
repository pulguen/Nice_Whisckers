from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from apps.barberia.models import Barberia
from apps.profesional.models import Profesional
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
        profesionales = Profesional.objects.filter(barberia=barberia)
        context['barberia'] = barberia
        context['posts'] = posts
        context['barberos'] = profesionales        
        return context

    
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        propietario = get_object_or_404(Propietario, barberia=post.propietario.barberia, propietario=request.user)        
        if post.propietario == propietario:
            post.delete()        
        return redirect('admin_barber', id=propietario.barberia.id)