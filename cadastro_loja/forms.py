from django import  forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime


class Cadastro_lojaForms(forms.Form):
    nome = forms.CharField            (label='Nome', max_length=100)
    celular = forms.CharField         (label='Celular', max_length=100)
    data_nascimento = forms.DateField (label='Data de Nascimento', widget=DatePicker())
    endereco = forms.CharField       (label='Endereço', max_length=100)
    bairro = forms.CharField          (label='Bairro', max_length=100)
    cep = forms.CharField             (label='CEP', max_length=8)
    referencia = forms.CharField      (label='Referência', max_length=100)
    email = forms.EmailField          (label='E-mail', max_length=150)

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if any(char.isdigit() for char in nome):
            raise forms.ValidationError('Nome inválido: não incluir números.')
        else:
            return nome