from django.urls import path
from .views import (
    NuevoTurnoView,
    ElegirBarberiaView,
    ElegirProfesionalView,
    ConfirmarTurnoView,
    ConfirmacionTurnoView
)

app_name = 'turno'

urlpatterns = [
    path('nuevo/', NuevoTurnoView.as_view(template_name='nuevo_turno.html'), name='nuevo_turno'),
    path('elegir-barberia/', ElegirBarberiaView.as_view(), name='elegir_barberia'),
    path('elegir-profesional/', ElegirProfesionalView.as_view(), name='elegir_profesional'),
    path('confirmar-turno/', ConfirmarTurnoView.as_view(), name='confirmar_turno'),
    path('<int:id>/', ConfirmacionTurnoView.as_view(), name='confirmacion_turno'),
]
