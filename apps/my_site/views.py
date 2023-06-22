from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.post.models import Post

class HomeView(LoginRequiredMixin, CreateView):
    def get(self, request):
        posts = Post.objects.all().order_by('-fecha_publicacion')
        context = {
            "user": request.user,
            "posts": posts  # Agrega el contexto "posts"
        }
        return render(request, 'core/home.html', context)
