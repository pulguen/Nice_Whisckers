from django.urls import path

from apps.profesional.views import ProfesionalCreateView

app_name= 'profesional'

urlpatterns = [
    path("crear/",ProfesionalCreateView.as_view(template_name='create_profesional.html'), name="create_profesional"),
]