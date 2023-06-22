from django.urls import path
from apps.turno.views import TurnosView, BarberiaView, BarberiaFormView

urlpatterns = [
    path("", TurnosView.as_view(), name="index_turno"),
    path("<int:id>", BarberiaView.as_view(), name="perfil_barberia"),
    path("crear", BarberiaFormView.as_view(), name="crear_barberia"),
]

