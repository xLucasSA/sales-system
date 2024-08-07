from django.urls import path
from .views import *

urlpatterns = [
    path('logout', logout_veiw, name='logout'),
    path('vendas', vendas, name='vendas'),
    path('checkout', checkout, name='checkout'),
    path('venda-gerada', gerar_venda, name='venda_finalizada'),
    path('relatorio-vendas', relatorio_vendas, name='relatorio_vendas'),
    path('graficos-vendas', gerar_graficos, name='graficos_vendas'),
    path('exportar-vendas', exportar_para_excel, name='exportar_vendas')
]