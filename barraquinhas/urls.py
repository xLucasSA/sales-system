from django.urls import path
from .views import login_view, vendas

urlpatterns = [
    path('login', login_view, name='login'),
    path('vendas', vendas, name='vendas'),
]