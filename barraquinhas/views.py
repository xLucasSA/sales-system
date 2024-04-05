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
    id_produtos: list[int] = []

    for produto in produtos:
        categoria = produto.get_categoria_display()

        if categoria in categorias.keys():
            categorias[categoria].append(produto)
        else:
            categorias[categoria] = [produto]

        id_produtos.append(produto.id_produto)

    context= {
        'categorias': categorias,
        'id_produtos': id_produtos
    }

    return render(request, 'barraquinhas/vendas.html', context)

def checkout(request):
    if request.method == 'POST':
        context = {
            "total_pedido": 0,
            "produtos" : {}
        } 
        for id_produto, quantidade in request.POST.items():
            
            if id_produto != 'csrfmiddlewaretoken':
                produto = Produtos.objects.get(id_produto=id_produto)

                context['produtos'][id_produto]= {
                    "produto": produto,
                    "valor": produto.valor,
                    "quantidade": quantidade
                }

                context['total_pedido'] += int(quantidade) * produto.valor
                

    return render(request, 'barraquinhas/checkout.html', context)