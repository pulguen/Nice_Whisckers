from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from apps.post.forms import PostForm
from apps.post.models import Post

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('index_post')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostsView(LoginRequiredMixin, TemplateView):
    template_name = 'index_posts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Posts'] = Post.objects.all()
        return context
    
class PostView(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vamos a buscar al alumno que esta relacionado con quien inicia sesion
        post_id = kwargs['id']
        post = Post.objects.get(id=post_id, user=self.request.user)
        if not Post:
            pass
            # Redirect al inicio PAGINA_INICIO
            # return Response(401, {"data": "Este usuario no es tuyo, no se puede acceder."})
        context['Post'] = post
        return context