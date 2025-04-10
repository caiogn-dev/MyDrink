from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        } 