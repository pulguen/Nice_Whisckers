from django.contrib import admin

# Register your models here.
from apps.usuario.models import CustomUser

@admin.register(CustomUser)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','email','es_propietario','es_profesional')