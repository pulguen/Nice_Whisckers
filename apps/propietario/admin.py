from django.contrib import admin

# Register your models here.
from apps.propietario.models import Propietario

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('propietario','barberia',)
    search_fields = ('propietario',)
    list_filter = ('propietario',)