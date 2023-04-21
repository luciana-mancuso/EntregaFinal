from django import forms
from AppCoder.models import Destino, Alojamiento, Comentario




class DestinoForm(forms.ModelForm):
    class Meta: 
        model= Destino
        fields="__all__"


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'correo_electronico', 'comentario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Ingrese su nombre'})
        self.fields['correo_electronico'].widget.attrs.update({'placeholder': 'Ingrese su correo electrónico'})
        self.fields['comentario'].widget.attrs.update({'placeholder': 'Ingrese su comentario aquí'})


class AlojamientoForm(forms.ModelForm):
    class Meta: 
        model= Alojamiento
        fields="__all__"

class BusquedaDestinoForm(forms.Form):
    titulo=forms.CharField(max_length=100)
