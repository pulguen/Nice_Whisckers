from django.db import models
from apps.my_site.models import Persona


# Create your models here.
class Propietario(Persona):
    barberia = models.ForeignKey("barberia.Barberia", verbose_name=("Barberia"), on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('dni',)
        
    def __str__(self):        
        return f"nombre propietario: {self.nombre}"
    
    