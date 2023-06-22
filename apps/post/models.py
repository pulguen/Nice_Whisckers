from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    propietario = models.ForeignKey("propietario.Propietario", verbose_name=("Propietario"),default=None, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='images/post', default='images/post/default_image.jpg',null=True,blank=True)
    
    class Meta:
        ordering = ('propietario',)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.barberia}"

class Megusta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fecha_me_gusta = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('usuario',)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Otros campos relacionados con el comentario    
    
    class Meta:
        ordering = ('usuario',)