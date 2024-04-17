from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now as dateNow

from ...models import Vendas, ItensVenda
from django.db.models import Q
import datetime


@login_required(login_url="login")
def historico_vendas(request):
    user = request.user

    if user.is_staff:
        pass
    
    registros = Vendas.objects.filter(id_vendedor=user.id, data_venda=dateNow().date())
    id_vendas = []

    for registro in registros:
        registro.data_venda = datetime.date.strftime(registro.data_venda, "%d/%m/%Y")
        id_vendas.append(registro.id_venda)
    
    produtos = ItensVenda.objects.filter(Q())

    return render(request, 'historico_vendas.html', {'registros': registros})