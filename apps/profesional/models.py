from django.db import models

# Create your models here.
class Profesional(models.Model):
    is_active = models.BooleanField(default=True)
    tipo_usuario = "Profesional"
    profesional_nombre = models.CharField(max_length=255)
    profesional_barberia = models.CharField(max_length=255)
    profesional_horarios = models.CharField(max_length=255)
    
    def __str__(self):        
        return f"nombre profesional: {self.profesional_nombre}"
    