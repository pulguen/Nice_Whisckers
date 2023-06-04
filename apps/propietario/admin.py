from django.contrib import admin

# Register your models here.
from apps.propietario.models import Propietario

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('propietario_nombre','propietario_barberia')
    search_fields = ('propietario_nombre',)
    list_filter = ('propietario_nombre',)