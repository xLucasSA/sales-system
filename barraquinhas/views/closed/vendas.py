from ...models import Produtos
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login") 
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

    return render(request, 'vendas.html', context)