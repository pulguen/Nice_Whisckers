from django.db import models

# Create your models here.
class Barberia(models.Model):
    barberia_nombre = models.CharField(max_length=100, null=True, blank=True)
    barberia_direccion = models.CharField(max_length=255, null=True, blank=True)
    barberia_horario = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ('barberia_nombre',)
    
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.barberia_nombre}"