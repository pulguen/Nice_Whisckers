from django.urls import path
from apps.propietario.views import AdminBarberView

app_name = 'propietario'

urlpatterns = [
    path('admin_barberia/<int:id>/', AdminBarberView.as_view(template_name='index_propietario.html'), name="admin_barber"),
]