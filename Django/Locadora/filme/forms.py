# forms.py

from django import forms
from .models import Filmes

class FormFilme(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = ['filme','genero', 'quantidade', 'preco']
        widgets = {
            'filme': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }