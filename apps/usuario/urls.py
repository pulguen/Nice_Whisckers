from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from apps.usuario.views import SignupView, UsuarioView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(template_name='singup.html'), name='singup'),
    path('perfil/', UsuarioView.as_view(template_name='perfil_usuario.html'), name='perfil_usuario'),
]