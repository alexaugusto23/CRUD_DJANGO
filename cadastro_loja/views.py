from django.shortcuts import render
from cadastro_loja.forms import  Cadastro_lojaForms

def index(request):
    form =  Cadastro_lojaForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    
    if request.method  == 'POST':
        form = Cadastro_lojaForms(request.POST)
        contexto = {'form':form}
        return render(request, 'consulta.html', contexto)
    else:
        return render(request, 'consulta.html')
