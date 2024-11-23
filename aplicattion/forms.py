
# comentarios/forms.py
from django import forms

from .models import *


class DptoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['cod_dpto', 'nombre_dpto']

class MpioForm(forms.ModelForm):
    class Meta:
        model = municipio
        fields = ['cod_mpio', 'nombre_mun','cod_dpto']

class SucForm(forms.ModelForm):
    class Meta:
        model = sucursal
        fields = ['sucursal_id', 'direccion','cod_mun']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class PrendaForm(forms.ModelForm):
    class Meta:
        model = prenda
        fields = '__all__'

class ArmarioForm(forms.ModelForm):
    class Meta:
        model = armario
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = '__all__'

class LavadoraForm(forms.ModelForm):
    class Meta:
        model = lavadora
        fields = '__all__'




class ComentarioForm(forms.Form):
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tus comentarios aquí...', 'rows': 6, 'cols': 40}),
        required=False  # Si es obligatorio, cambia esto a `True`
    )
    
    # Añadimos un campo con opciones de radio buttons
    LAVADO_CHOICES = [
        ('normal', 'Lavado Normal'),
        ('intermedio', 'Lavado Intermedio'),
        ('full', 'Lavado Full'),
    ]
    
    lavado = forms.ChoiceField(
        choices=LAVADO_CHOICES,
        widget=forms.RadioSelect,  # Usamos RadioSelect para que se muestren como radio buttons
        required=True  # Hacemos este campo obligatorio
    )