from django.db import models
from django.http import HttpRequest
from nice_whisckers import settings
#from django.contrib.auth import get_user_model
from django.utils.functional import lazy


#def get_current_user_id():
#    request = HttpRequest()
#    return get_user_model().objects.get(id=request.user.id)

class Turno(models.Model):
    barberia = models.ForeignKey('barberia.barberia', verbose_name=("Barberia"), on_delete=models.CASCADE)
    profesional = models.ForeignKey('profesional.Profesional', verbose_name=("Profesional"), on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    comentario = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ["-dia"]

        
