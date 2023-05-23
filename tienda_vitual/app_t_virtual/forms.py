from django import forms
from django.core.exceptions import ValidationError
from .models import Clientes

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre", 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=256,
    )
    apellido = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=256,
    )
    email = forms.EmailField(
        label="Email", 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        # max_length=256,        
    )
    mensaje =forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        required=True,
        max_length=256,
    )

class AltaClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Mail", required=True)
    telefono = forms.CharField(label="telefono", required=True)
    dni = forms.IntegerField(label="dni",required=True)

    def clean(self):
        # Validar si ya existe
        if Clientes.objects.filter(dni=self.cleaned_data["dni"]).exists():
            raise ValidationError("Ya existe un Cliente con ese DNI")
        
class AltaClienteFormModel(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ["nombre","apellido","email","telefono","dni"]
