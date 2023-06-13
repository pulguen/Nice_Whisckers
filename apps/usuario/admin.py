from django.contrib import admin

# Register your models here.
from apps.usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nickname',)
    search_fields = ('nickname',)
