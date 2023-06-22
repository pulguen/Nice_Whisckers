
from django.db import models

from nice_whisckers import settings

# Create your models here.
class Propietario(models.Model):
    propietario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=("barberia"), 
        on_delete=models.CASCADE,
        default=None,
        related_name='barberia',
        null=True,
        blank=True,
        )
    barberia = models.ForeignKey(
        "barberia.Barberia", 
        verbose_name=("barberia"), 
        on_delete=models.CASCADE,
        default=None,
        related_name='barberia',
        null=True,
        blank=True,
        )
    
    class Meta:
        ordering = ('propietario',)