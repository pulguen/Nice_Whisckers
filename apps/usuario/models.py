# Create your models here.
from django.db import models

class Usuario (models.Model):
    nickname = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    propietario = models.BooleanField(default=False)
    profesional = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('nickname',)
    
    def __str__(self):
        return self.usuario
    
    
    