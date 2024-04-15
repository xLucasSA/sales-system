from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .forms import *
from django.utils.timezone import now as dateNow
import datetime
from django.db.models import Q
import pytz

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def login_view(request):
    
    if request.method == "GET":
        user = request.user
        
        if user.is_authenticated:
            return redirect('index')

        return render(request, 'login.html')
    
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  
         
        else:
            return render(request, "login.html", context={"mensagem":"Login ou senha incorreta"})  

def logout_veiw(request):
    logout(request)
    
    return redirect('login')

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

@login_required(login_url="login") 
def checkout(request):
    if request.method == 'POST':
        context = {
            "total_pedido": 0,
            "pedido" : [],
            "form": FormaPagamento()
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

    return render(request, 'checkout.html', context)


@login_required(login_url="login")
def gerar_venda(request):
    
    if request.method == "POST":
        dados_venda = {
            'id_vendedor': request.user.id,
            'data_venda': dateNow().astimezone(tz=pytz.timezone('America/Sao_Paulo')).date(),
            'ativo': True,
        }
        itens_vendidos = {}


        for id, quantidade in request.POST.items():
            if id == 'forma_pagamento':
                dados_venda['forma_pagamento'] = int(quantidade)

            elif id == 'valor_total':
                dados_venda['valor_total'] = float(quantidade)

            else:
                if id != 'csrfmiddlewaretoken':
                    itens_vendidos[id] = quantidade

        venda_realizada = VendasForm(dados_venda)

        if venda_realizada.is_valid():
            venda_registrada = venda_realizada.save()
            
            for item, quantidade in itens_vendidos.items():
                item_venda = {
                    'id_produto': item,
                    'quantidade': quantidade,
                    'id_venda': venda_registrada.id_venda
                }

                registro_item_venda = ItensVendasForm(item_venda)
                
                if registro_item_venda.is_valid():
                    registro_item_venda.save()

            return redirect('vendas')
                

        #informar que houve erro ao registrar a venda 
      
@login_required(login_url="login")
def historico_vendas(request):
    user = request.user

    if user.is_staff:
        pass
    
    registros = Vendas.objects.filter(id_vendedor=user.id, data_venda=dateNow())
    id_vendas = []

    for registro in registros:
        registro.data_venda = datetime.date.strftime(registro.data_venda, "%d/%m/%Y")
        id_vendas.append(registro.id_venda)
        

    return render(request, 'historico_vendas.html', {'registros': registros})