from django import forms
from AppCoder.models import Destino, Alojamiento




class DestinoForm(forms.ModelForm):
    class Meta: 
        model= Destino
        fields="__all__"

class AlojamientoForm(forms.ModelForm):
    class Meta: 
        model= Alojamiento
        fields="__all__"

class BusquedaDestinoForm(forms.Form):
    titulo=forms.CharField(max_length=100)
