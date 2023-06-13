from django.db import models

# Create your models here.
class Barberia(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    horario = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.barberia_nombre}"