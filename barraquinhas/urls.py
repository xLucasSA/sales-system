from django.urls import path
from .views import login_view, vendas, checkout

urlpatterns = [
    path('login', login_view, name='login'),
    path('vendas', vendas, name='vendas'),
    path('checkout', checkout, name='checkout')
]