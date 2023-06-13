from django.db import models

# Create your models here.
class Post(models.Model):
    barberia = models.ForeignKey('barberia.Barberia', on_delete=models.CASCADE)
    autor = models.ForeignKey('propietario.Propietario', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Otros campos relacionados con el post
    
    class Meta:
        ordering = ('barberia',)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.barberia}"

class Megusta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    fecha_me_gusta = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('usuario',)


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Otros campos relacionados con el comentario    
    
    class Meta:
        ordering = ('usuario',)