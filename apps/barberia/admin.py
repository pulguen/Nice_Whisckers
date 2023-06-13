from django.contrib import admin

# Register your models here.
from apps.barberia.models import Barberia

@admin.register(Barberia)
class BarberiaAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion",)
    search_fields = ('nombre',)
    list_filter = ('nombre',)