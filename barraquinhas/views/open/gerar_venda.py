from ...forms import VendasForm, ItensVendasForm
from django.shortcuts import redirect
from django.utils.timezone import now as dateNow
import pytz

def gerar_venda(request):
    
    if request.method == "POST":
        dados_venda = {
            'data_venda': dateNow().astimezone(tz=pytz.timezone('America/Sao_Paulo')).date(),
        }
        itens_vendidos = {}


        for id, quantidade in request.POST.items():
            if id == 'forma_pagamento':
                dados_venda['forma_pagamento'] = int(quantidade)

            elif id == 'valor_total':
                dados_venda['valor_total'] = float(quantidade)

            elif id != 'csrfmiddlewaretoken':
                itens_vendidos[id] = quantidade

        venda_realizada = VendasForm(dados_venda)

        if venda_realizada.is_valid():
            venda_registrada = venda_realizada.save()
            
            for item, quantidade_e_valor_unitario in itens_vendidos.items():
                quantidade = quantidade_e_valor_unitario.split(' X ')[0]
                valor_unitario = quantidade_e_valor_unitario.split(' X ')[1]

                item_venda = {
                    'id_produto': item,
                    'quantidade': float(quantidade),
                    'valor_unitario': float(valor_unitario),
                    'id_venda': venda_registrada.id_venda
                }

                registro_item_venda = ItensVendasForm(item_venda)
                
                if registro_item_venda.is_valid():
                    registro_item_venda.save()

            return redirect('vendas')
                

        #informar que houve erro ao registrar a venda 