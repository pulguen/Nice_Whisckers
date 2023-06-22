from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    es_propietario = models.BooleanField(default=False)
    es_profesional = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
