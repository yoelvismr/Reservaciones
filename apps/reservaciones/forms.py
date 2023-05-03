from django import forms

from apps.reservaciones.models import *


class ReservacionGastronmicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_cliente'].widget.attrs['autofocus'] = True

    class Meta:
        model = ReservacionGastronmica
        fields = '__all__'
        widgets = {
            'nombre_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': ' Ingrese el nombre',
                }
            ),
            'cantidad_persona': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad de persona',
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha',
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese hora',
                }
            ),
        }
