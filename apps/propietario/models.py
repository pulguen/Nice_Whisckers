from django.db import models

# Create your models here.
class Propietario(models.Model):
    tipo_usuario = "Propietario"
    propietario_is_active = models.BooleanField(default=True,verbose_name="Activo")
    propietario_nombre = models.CharField(max_length=255,verbose_name="Nombre")
    propietario_barberia =models.CharField(max_length=255,verbose_name="Barberia")
    propietario_ciut = models.IntegerField(null=True,blank=True,verbose_name="Cuit")
        
    def __str__(self):        
        return f"nombre profesional: {self.propietario_nombre}"
    
    