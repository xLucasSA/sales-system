from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Produtos

def index(request):
    return render(request, 'index.html')

def login_view(request):

    if request.method == "GET":
        return render(request, 'login.html')
    
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('vendas')  
         
        else:
            return render(request, "login.html", context={"mensagem":"Login ou senha incorreta"})  

@login_required(login_url="/login") 
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

@login_required(login_url="/login") 
def checkout(request):
    if request.method == 'POST':
        context = {
            "total_pedido": 0,
            "pedido" : []
        } 

        for id_produto, quantidade in request.POST.items():

            if id_produto != 'csrfmiddlewaretoken':
                produto = Produtos.objects.get(id_produto=id_produto)

                context['pedido'].append({
                    "id": produto.id_produto,
                    "produto": produto.nome,
                    "valor_unitario": produto.valor,
                    "quantidade": quantidade,
                    "valor_final": float(quantidade) * produto.valor
                })

                context['total_pedido'] += float(quantidade) * produto.valor
    print(request.body)
    return render(request, 'checkout.html', context)


@login_required(login_url="/login")
def gerar_venda(request):
    print(request.body)

    return redirect('vendas')