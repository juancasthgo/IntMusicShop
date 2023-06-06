from django import forms
from .models import Categoria, Contacto, Producto

class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('categoria', 'fecha', 'titulo', 'descripcion', 'precio', 'imagen', 'urlpago')
        widgets = {
            'categoria': forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "categoria",
                }
            ),
            'fecha': forms.SelectDateWidget(
                attrs={
                    "class": "visually-hidden",
                }
            ),
            'titulo':forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "titulo",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "descripcion",
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "precio",
                }
            ),
            'urlpago': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": 'urlpago',
                }
            ),
            
            'imagen': forms.ClearableFileInput(),
        }


# FORMULARIO CONTACTO
class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=15) #VALIDACION 1
    class Meta:
        model = Contacto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
