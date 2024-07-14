from django import forms
from .models import produto

class Formulario(forms.Form):
    class Meta:
        model=produto
        fields=['tipo','nome','preco']