from django import forms
from apps.profesional.models import Profesional

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = [
            'nombre',
            'horarios',
        ]