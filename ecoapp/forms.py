from django import forms
from .models import Reciclaje, Plantacion

class ReciclajeForm(forms.ModelForm):
    class Meta:
        model = Reciclaje
        fields = ['tipo_material', 'peso_kg', 'punto_acopio']
        widgets = {
            'tipo_material': forms.Select(attrs={'class': 'form-select'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ej. 5.50'}),
            'punto_acopio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Centro Comunitario Norte'}),
        }

    def clean_peso_kg(self):
        peso = self.cleaned_data.get('peso_kg')
        if peso is not None and peso <= 0:
            raise forms.ValidationError("El peso debe ser mayor a 0 kg.")
        return peso

class PlantacionForm(forms.ModelForm):
    class Meta:
        model = Plantacion
        fields = ['especie_arbol', 'cantidad', 'ubicacion', 'fecha_plantacion']
        widgets = {
            'especie_arbol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pino, Encino'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Parque Morelos'}),
            'fecha_plantacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad < 1:
            raise forms.ValidationError("Debes registrar al menos 1 árbol.")
        return cantidad
