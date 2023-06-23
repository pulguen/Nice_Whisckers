from django.db import models

# Create your models here.
class Profesional(models.Model):
    nombre = models.CharField(max_length=50,default='barbero',null=True,blank=True)
    disponible = models.BooleanField(default=True)
    horarios = models.CharField(max_length=255)
    barberia =models.ForeignKey("barberia.Barberia", verbose_name=("Barbería"), on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = 'Profesionales'
    
    def __str__(self):        
        return f"nombre profesional: {self.nombre}"

