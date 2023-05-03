import re
import datetime
from django import forms
from django.core.exceptions import ValidationError

from apps.dashboard.models import Categoria, Entidad


class CategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': ' Ingrese el nombre',
                }
            ),
        }


class EntidadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Entidad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'row': 2,
                }
            ),
        }


class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = ['imagen']
        exclude = ['entidad']
