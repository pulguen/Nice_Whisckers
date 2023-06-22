from django.db import models
from apps.usuario.models import CustomUser

class PersonaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(
            #deleted_at__isnull=False,
            active=False
        )

class Persona(models.Model):
    class Meta:
        # Significa que no se va a crear una tabla llamada Persona.
        abstract = True
            
    nombre = models.CharField(max_length=50,default='')
    apellido = models.CharField(max_length=50,default='')
    dni = models.IntegerField(null=True,blank=True)
    email = models.EmailField(default='')
    active = models.BooleanField(default=True)
    objects_all = models.Manager()
    objects = PersonaManager()
    user = models.ForeignKey(CustomUser, verbose_name=("Usuario"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.dni}' 
    