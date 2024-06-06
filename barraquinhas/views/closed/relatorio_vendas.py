from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def relatorio_vendas(request):
    return render(request, 'relatorio_vendas.html')