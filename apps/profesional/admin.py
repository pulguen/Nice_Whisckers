from django.contrib import admin

# Register your models here.
from apps.profesional.models import Profesional

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('profesional_nombre',)
    search_fields = ('profesional_nombre',)
    list_filter = ('profesional_nombre',)