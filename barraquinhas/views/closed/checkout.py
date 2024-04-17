from ...forms import FormaPagamento
from ...models import Produtos
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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