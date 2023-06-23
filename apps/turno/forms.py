import datetime
from django import forms
from django.forms import DateInput, TimeInput
from datetime import date, timedelta
from apps.barberia.models import Barberia
from apps.profesional.models import Profesional
from apps.turno.models import Turno
from django.core.exceptions import ValidationError
from django.utils import timezone


class NuevoTurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = [
            'dia',
            'hora',
        ]
        widgets = {
            'dia': DateInput(attrs={'type': 'date'}),
            'hora': TimeInput(attrs={'type': 'time', 'step': '1800'}),
        }

    def clean_dia(self):
        dia = self.cleaned_data.get('dia')
        if dia:
            if dia.weekday() >= 5:
                raise forms.ValidationError("Solo se permiten días de lunes a viernes.")
            min_date = self.get_min_date()
            if dia < min_date:
                raise forms.ValidationError("Selecciona una fecha a partir del próximo lunes.")
        dia_local = timezone.make_aware(datetime.datetime.combine(dia, datetime.time.min))
        return timezone.localtime(dia_local).strftime('%Y-%m-%d')

    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        if hora and (hora.hour < 9 or hora.hour > 18 or hora.minute not in [0, 30]):
            raise forms.ValidationError("La hora debe estar entre las 9 y las 18 y los minutos deben ser 0 o 30.")
        return hora.strftime('%H:%M:%S')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dia'].widget.attrs['min'] = self.get_min_date().strftime('%Y-%m-%d')
        self.fields['dia'].widget.attrs['onkeydown'] = 'return false'  # Desactiva la entrada por teclado

    @staticmethod
    def get_min_date():
        today = date.today()
        days_ahead = (0 - today.weekday()) % 7  # 0 representa el lunes (0-6: lunes-domingo)
        min_date = today + timedelta(days=days_ahead)
        return min_date


class ElegirBarberiaForm(forms.Form):
    barberia = forms.ModelChoiceField(queryset=Barberia.objects.all())

class ElegirProfesionalForm(forms.Form):
    profesional = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        barberia = kwargs.pop('barberia')
        super().__init__(*args, **kwargs)
        self.fields['profesional'].queryset = Profesional.objects.filter(barberia=barberia)
        self.fields['profesional'].label_from_instance = lambda obj: obj.nombre

class ConfirmarTurnoForm(forms.Form):
    dia = forms.DateField(widget=forms.HiddenInput())
    hora = forms.TimeField(widget=forms.HiddenInput())
    barberia_id = forms.IntegerField(widget=forms.HiddenInput())
    profesional_id = forms.IntegerField(widget=forms.HiddenInput())
