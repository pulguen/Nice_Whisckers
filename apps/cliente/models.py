from django.db import models

# Create your models here.
class Cliente(models.Model):
    is_active = models.BooleanField(default=True)
    tipo_usuario = "cliente"
    cliente_nombre = models.CharField(max_length=100, null=True, blank=True)
    cliente_direccion = models.CharField(max_length=255, null=True, blank=True)
    cliente_telefono = models.IntegerField()
    
    class Meta:
        ordering = ('cliente_nombre',)
    
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.cliente_nombre}"
