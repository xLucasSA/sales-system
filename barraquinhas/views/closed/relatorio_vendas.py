from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt

from barraquinhas.models import *
from django.db.models import Sum, Q

from django.http import JsonResponse
import json

@staff_member_required
def relatorio_vendas(request):
    return render(request, 'relatorio_vendas.html')

@csrf_exempt
@staff_member_required
def gerar_graficos(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        grafico = body_data.get('nomeGrafico')

        graficos = {
            'quantidadeVendida': grafico_quantidades(),
            'valorArrecadado': grafico_valor_arrecadado()
        }
        
        return graficos[grafico]


def grafico_quantidades():
    itens_vendidos = ItensVenda.objects.prefetch_related('id_venda').all()
    nome_produtos = Produtos.objects.values_list('nome', flat=True).order_by('nome')
    datas = Vendas.objects.distinct().values_list('data_venda', flat=True)

    quantidade_vendida = {}

    for produto in nome_produtos:
        for data in datas:
            quantidade_vendida_query = itens_vendidos.filter(
                Q(id_venda__data_venda=data) & 
                Q(id_produto__nome=produto)
                ).exclude(id_venda__forma_pagamento=5).aggregate(Sum('quantidade'))
            quantidade = quantidade_vendida_query.get('quantidade__sum')
        
            if not quantidade:
                continue
            
            quantidade_devolvida_query = itens_vendidos.filter(
                Q(id_venda__data_venda=data) & 
                Q(id_produto__nome=produto) &
                Q(id_venda__forma_pagamento=5)
                ).aggregate(Sum('quantidade'))
            devolucoes = quantidade_devolvida_query.get('quantidade__sum')
            
            if devolucoes:
                quantidade -= devolucoes

            if quantidade_vendida.get(produto):
                quantidade_vendida[produto] += quantidade
            else:
                quantidade_vendida[produto] = quantidade
            
    return JsonResponse(quantidade_vendida)


def grafico_valor_arrecadado():
    vendas_realizas = Vendas.objects.exclude(forma_pagamento=5)
    devolucoes_realizadas = Vendas.objects.filter(forma_pagamento=5)
    datas = Vendas.objects.distinct().values_list('data_venda', flat=True).order_by('data_venda')

    valores_vendidos = {}

    for data in datas:
        valor_dia = vendas_realizas.filter(data_venda=data).aggregate(Sum('valor_total')).get('valor_total__sum')
        
        if not valor_dia:
            continue

        devolucao_dia = devolucoes_realizadas.filter(data_venda=data).aggregate(Sum('valor_total')).get('valor_total__sum')

        if devolucao_dia:
            valor_dia -= devolucao_dia

        data = data.strftime('%d/%m/%Y')
        valores_vendidos[data] = valor_dia

    return JsonResponse(valores_vendidos)