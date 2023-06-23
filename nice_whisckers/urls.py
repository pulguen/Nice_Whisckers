"""
URL configuration for nice_whisckers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path as url
from apps.my_site.views import HomeView
# NW_VERSION = 'nw1'
# BASE_URL = f'{NW_VERSION}/'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('barberia/',include('apps.barberia.urls')),
    path('post/',include('apps.post.urls')),
    path('profesional/',include('apps.profesional.urls')),
    path('propietario/',include('apps.propietario.urls')),
    path('turno/',include('apps.turno.urls')), 
    path('usuario/',include('apps.usuario.urls')),
]
