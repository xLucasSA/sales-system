from ...forms import VendasForm, ItensVendasForm
from django.shortcuts import redirect
from django.utils.timezone import now as dateNow
import pytz

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