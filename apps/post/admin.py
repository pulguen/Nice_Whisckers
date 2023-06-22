from django.contrib import admin

# Register your models here.
from apps.post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('propietario','contenido','fecha_publicacion',)
