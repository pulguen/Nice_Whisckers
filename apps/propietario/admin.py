from django.contrib import admin

# Register your models here.
from apps.propietario.models import Propietario

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni','barberia')
    search_fields = ('dni',)
    list_filter = ('dni',)
    