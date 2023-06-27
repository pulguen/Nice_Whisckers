from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.post.models import Post
from apps.turno.models import Turno

class HomeView(LoginRequiredMixin, CreateView):
    def get(self, request):
        posts = Post.objects.all().order_by('-fecha_publicacion')
        turnos= Turno.objects.filter(usuario=self.request.user)
        context = {
            "user": request.user,
            "posts": posts,
            'turno':turnos,
        }
        return render(request, 'core/home.html', context)
