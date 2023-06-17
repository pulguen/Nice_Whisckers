from django.db import models
from apps.my_site.models import Persona

# Create your models here.
class Profesional(Persona):
    disponible = models.BooleanField(default=True)
    horarios = models.CharField(max_length=255)
    barberia =models.ForeignKey("barberia.Barberia", verbose_name=("Berbería"), on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('dni',)
        verbose_name_plural = 'Profesionales'
    
    def __str__(self):        
        return f"nombre profesional: {self.nombre}"