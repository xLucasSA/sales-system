from django.db import models
from django.utils.timezone import now as dateNow
from django.contrib.auth.models import User
import pytz

class Produtos(models.Model):
    class Categoria(models.TextChoices):
        ALIMENTOS = 'A', 'Alimentos'
        BEBIDAS = 'B', 'Bebidas'
        JOGOS = 'J', 'Jogos'
        DOACAO = 'D', 'Doação'
        OUTROS = 'O', 'Outros'

    class Medida(models.TextChoices):
        ML = 'ml', 'ml'
        UNIDADE = 'un', 'Unidade'
        KILOGRAMA = 'kg', 'Kg'
        LATA = 'lt', 'Lata'
        OUTROS = 'ot', 'Outros'

    id_produto = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=200, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    categoria = models.CharField(max_length=1, choices=Categoria.choices, default=Categoria.OUTROS)
    ativo = models.BooleanField(null=False, blank=False, default=True)
    medida = models.CharField(max_length=2, choices=Medida.choices, default=Medida.OUTROS)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name_plural = "Produtos"
    
class Vendas(models.Model):
    class Pagamento(models.IntegerChoices):
        DINHEIRO = 1, 'Dinheiro'
        DEBITO = 2, 'Catão de Débito'
        CREDITO = 3, 'Cartão de Crédito'
        PIX = 4, 'PIX'
        DEVOLUCAO = 5, 'Devolução'

    id_venda = models.AutoField(primary_key=True, unique=True)
    data_venda = models.DateField(null=False, blank=False, default=dateNow().astimezone(tz=pytz.timezone('America/Sao_Paulo')).date())
    forma_pagamento = models.IntegerField(null=False, blank=False, default=Pagamento.DINHEIRO, choices=Pagamento.choices)
    valor_total = models.FloatField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "Vendas"
        ordering = ['-data_venda']

class ItensVenda(models.Model):
    id_venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)