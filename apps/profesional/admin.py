from django.contrib import admin

# Register your models here.
from apps.profesional.models import Profesional

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni')
    search_fields = ('dni',)
    list_filter = ('dni',)