from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt

from barraquinhas.models import *
from django.db.models import Sum, Q

from django.http import JsonResponse
import json

from openpyxl import Workbook
from django.http import HttpResponse

@staff_member_required
def relatorio_vendas(request):
    datas = Vendas.objects.distinct().values_list('data_venda', flat=True)
    
    context = {
        'data_fim': datas[0].strftime('%Y-%m-%d'),
        'data_inicio': datas[len(datas) - 1].strftime('%Y-%m-%d')
    }

    return render(request, 'relatorio_vendas.html', context)

@csrf_exempt
@staff_member_required
def gerar_graficos(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            grafico = body_data.get('nomeGrafico')
            data_inicio = body_data.get('data_inicio')
            data_fim = body_data.get('data_fim')

            graficos = {
                'quantidadeVendida': grafico_quantidades(data_inicio, data_fim),
                'valorArrecadado': grafico_valor_arrecadado(data_inicio, data_fim)
            }
            
            return graficos[grafico]
        except:
            return render(request, 'relatorio_vendas.html')


def grafico_quantidades(data_inicio, data_fim):
    itens_vendidos = ItensVenda.objects.prefetch_related('id_venda').all()
    nome_produtos = Produtos.objects.values_list('nome', flat=True).order_by('nome')
    datas = Vendas.objects.filter(
        Q(data_venda__gte=data_inicio, data_venda__lte=data_fim)
    ).distinct().values_list('data_venda', flat=True)

    quantidade_vendida = {}

    for produto in nome_produtos:
        for data in datas:
            quantidade_vendida_query = itens_vendidos.filter(
                Q(id_venda__data_venda=data) & 
                Q(id_produto__nome=produto)
                ).exclude(id_venda__forma_pagamento=5).aggregate(Sum('quantidade'))
            quantidade = quantidade_vendida_query.get('quantidade__sum')

            quantidade_devolvida_query = itens_vendidos.filter(
                Q(id_venda__data_venda=data) & 
                Q(id_produto__nome=produto)
                ).filter(id_venda__forma_pagamento=5).aggregate(Sum('quantidade'))
            devolucoes = quantidade_devolvida_query.get('quantidade__sum')

            if devolucoes:
                if not quantidade:
                    quantidade = -devolucoes
                else:
                    quantidade -= devolucoes

            if quantidade:
                if quantidade_vendida.get(produto):
                    quantidade_vendida[produto] += quantidade
                else:
                    quantidade_vendida[produto] = quantidade
            
    return JsonResponse(quantidade_vendida)


def grafico_valor_arrecadado(data_inicio, data_fim):
    vendas_realizas = Vendas.objects.exclude(forma_pagamento=5)
    devolucoes_realizadas = Vendas.objects.filter(forma_pagamento=5)
    datas = Vendas.objects.filter(
        Q(data_venda__gte=data_inicio, data_venda__lte=data_fim)
    ).distinct().values_list('data_venda', flat=True).order_by('data_venda')

    valores_vendidos = {}

    for data in datas:
        valor_dia = vendas_realizas.filter(data_venda=data).aggregate(Sum('valor_total')).get('valor_total__sum')

        devolucao_dia = devolucoes_realizadas.filter(data_venda=data).aggregate(Sum('valor_total')).get('valor_total__sum')

        if devolucao_dia:
            if not valor_dia:
                valor_dia = -devolucao_dia
            else:
                valor_dia -= devolucao_dia

        if valor_dia:
            data = data.strftime('%d/%m/%Y')
            valores_vendidos[data] = valor_dia

    return JsonResponse(valores_vendidos)

@staff_member_required
def exportar_para_excel(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    itens_vendidos = ItensVenda.objects.prefetch_related('id_venda').filter(id_venda__data_venda__gte=data_inicio, id_venda__data_venda__lte=data_fim)

    wb = Workbook()
    ws = wb.active
    
    cabecalhos = ['Nome Produto', 'Quantidade Vendida', 'Valor Unitário', 'Forma Pagamento', 'Data Venda']
    ws.append(cabecalhos)

    for registro in itens_vendidos:
        linha = [
            registro.id_produto.nome,
            registro.quantidade,
            registro.valor_unitario,
            registro.id_venda.get_forma_pagamento_display(),
            registro.id_venda.data_venda.strftime('%d/%m/%Y'),
        ]
        ws.append(linha)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=registros_vendas_barraquinhas.xlsx'
    wb.save(response)

    return response