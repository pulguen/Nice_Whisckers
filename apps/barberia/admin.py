from django.contrib import admin

# Register your models here.
from apps.barberia.models import Barberia

@admin.register(Barberia)
class BarberiaAdmin(admin.ModelAdmin):
    list_display = ("barberia_nombre","barberia_direccion",)
    search_fields = ('barberia_nombre',)
    list_filter = ('barberia_nombre',)