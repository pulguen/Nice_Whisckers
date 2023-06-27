from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2',)
        
        
