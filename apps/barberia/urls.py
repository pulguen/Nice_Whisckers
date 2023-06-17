from django.urls import path

from apps.barberia.views import BarberiasView, BarberiaView, BarberiaFormView

urlpatterns = [
    path("", BarberiasView.as_view(), name="index_barberias"),
    path("<int:id>", BarberiaView.as_view(), name="perfil_barberia"),
    path("crear", BarberiaFormView.as_view(), name="crear_barberia"),
]

