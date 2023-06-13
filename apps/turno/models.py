from django.db import models

# Create your models here.
class Turno(models.Model):
    cliente = models.ForeignKey('usuario.Usuario', verbose_name=("Usuario"), on_delete=models.CASCADE)
    barberia = models.ForeignKey('barberia.barberia', verbose_name=("Barberia"), on_delete=models.CASCADE)
    profesional = models.ForeignKey('profesional.Profesional', verbose_name=("Profesional"), on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    comentario = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ('cliente',)