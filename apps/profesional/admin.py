from django.contrib import admin

# Register your models here.
from apps.profesional.models import Profesional

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'barberia')
    search_fields = ('nombre',)
    list_filter = ('nombre',)