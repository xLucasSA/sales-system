from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_veiw, name='logout'),
    path('vendas', vendas, name='vendas'),
    path('checkout', checkout, name='checkout'),
    path('venda-gerada', gerar_venda, name='venda_finalizada'),
    path('historico', historico_vendas, name='historico_vendas')
]