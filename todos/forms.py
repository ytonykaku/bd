# dentro de <sua_aplicacao>/forms.py
from django import forms
from .models import Jogador  # Certifique-se de importar o modelo correto

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = '__all__'  # Ou especifique os campos que deseja no formulário
