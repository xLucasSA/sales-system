from django.shortcuts import render
from django.contrib.auth import login
from .models import Produtos

def index(request):
    return render(request, 'barraquinhas/index.html')

def login_view(request):
    return render(request, 'barraquinhas/login.html')

def vendas(request):
    produtos = Produtos.objects.filter(ativo=True)

    categorias: dict[str, list] = {}

    for produto in produtos:
        categoria = produto.get_categoria_display()

        if categoria in categorias.keys():
            categorias[categoria].append(produto)
        else:
            categorias[categoria] = [produto]

    context= {
        'categorias': categorias
    }

    return render(request, 'barraquinhas/vendas.html', context)
