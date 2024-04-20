from django.shortcuts import render, redirect
from .models import usuarios
import requests

def home(request):
    return render(request, "usuarios/home.html")


def validar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  
        dados = resposta.json()
        return dados.get('erro') is None  
    except requests.RequestException:
        return False


def cadastrar_usuario(request):
    aviso = None 
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cep = request.POST.get('cep')  
        
  
        if validar_cep(cep):
            usuarios.objects.create(nome=nome, email=email, senha=senha, cep=cep)
            aviso = 'Cadastro realizado com sucesso!'
        else:
            aviso = 'O CEP fornecido é inválido.'
    
    return render(request, 'usuarios/home.html', {'aviso': aviso})



def usuarios_cadastrados(request):
    usuarios_cadastrados = usuarios.objects.all()
    context = {

        'usuarios_cadastrados': usuarios_cadastrados,
    }
    return render(request, 'usuarios/usuarios_cadastrados.html', context)


