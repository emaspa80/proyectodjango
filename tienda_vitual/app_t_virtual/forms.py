from django import forms

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