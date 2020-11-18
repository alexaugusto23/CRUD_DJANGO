from django import  forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from cadastro_loja.validation import *


class Cadastro_lojaForms(forms.Form):
    nome = forms.CharField            (label='Nome', max_length=100)
    celular = forms.CharField         (label='Celular', max_length=100)
    data_nascimento = forms.DateField (label='Data de Nascimento', widget=DatePicker())
    endereco = forms.CharField        (label='Endereço', max_length=100)
    bairro = forms.CharField          (label='Bairro', max_length=100)
    cep = forms.CharField             (label='CEP', max_length=8)
    referencia = forms.CharField      (label='Referência', max_length=100)
    email = forms.EmailField          (label='E-mail', max_length=150)

    def clean(self):
        nome = self.cleaned_data.get('nome')
        bairro = self.cleaned_data.get('bairro')
        referencia = self.cleaned_data.get('referencia')
        lista_de_erros = {}
        msgs_errors_campo_num(nome, 'nome', lista_de_erros)
        msgs_errors_campo_num(bairro, 'bairro', lista_de_erros)
        msgs_errors_campo_num(referencia, 'referencia', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro,mensagem_erro)
        return self.cleaned_data


'''
def clean_nome(self):
    nome = self.cleaned_data.get('nome')
    if any(char.isdigit() for char in nome_campo):
        raise forms.ValidationError('Nome inválido: não incluir números.')
    else:
        return nome
'''

