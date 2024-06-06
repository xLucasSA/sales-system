from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now as dateNow

from ...models import Vendas, ItensVenda
# from django.db.models import Q 
import datetime
import pytz

def historico_vendas(request):
    user = request.user

    if user.is_staff:
        pass
    
    registros = Vendas.objects.filter(id_vendedor=user.id, data_venda=dateNow().astimezone(tz=pytz.timezone('America/Sao_Paulo')).date())
    id_vendas = []

    for registro in registros:
        registro.data_venda = datetime.date.strftime(registro.data_venda, "%d/%m/%Y")

    return render(request, 'historico_vendas.html', {'registros': registros})
