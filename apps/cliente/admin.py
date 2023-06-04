from django.contrib import admin

# Register your models here.
from apps.cliente.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente_nombre','cliente_telefono')
    search_fields = ('cliente_nombre',)
    list_filter = ('cliente_nombre',)