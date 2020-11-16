from django import  forms

class Cadastro_lojaForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    celular = forms.CharField(label='Celular', max_length=100)
    data_nascimento = forms.DateField(label='Data de Nascimento')
    endereco = forms.DateField(label='Endereço')
    bairro = forms.CharField(label='Bairro', max_length=100)
    cep = forms.CharField(label='CEP', max_length=8)
    referencia = forms.CharField(label='Referência', max_length=100)
    email = forms.CharField(label='Email', max_length=100)


