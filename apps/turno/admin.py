from django.contrib import admin

# Register your models here.
from apps.turno.models import Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('usuario','barberia','profesional')
    search_fields = ('usuario',)
    list_filter = ('usuario',)
