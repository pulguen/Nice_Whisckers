from django import forms
from apps.barberia.models import Barberia

class BarberiaForm(forms.ModelForm):
    class Meta:
        model = Barberia
        fields = [
            'nombre',
            'direccion',
            'horario',
        ]
        
