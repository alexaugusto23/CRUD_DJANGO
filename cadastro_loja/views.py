from django.shortcuts import render
from cadastro_loja.forms import  Cadastro_lojaForms

def index(request):
    form =  Cadastro_lojaForms()
    contexto = {'form':form}
    return render(request,'index.html', contexto)