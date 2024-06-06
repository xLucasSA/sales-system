from django.urls import path
from .views import *

urlpatterns = [
    path('logout', logout_veiw, name='logout'),
    path('vendas', vendas, name='vendas'),
    path('checkout', checkout, name='checkout'),
    path('venda-gerada', gerar_venda, name='venda_finalizada'),
    path('relatorio-vendas', relatorio_vendas, name='relatorio_vendas')
]