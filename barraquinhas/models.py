from django.db import models
from django.utils.timezone import now as dateNow
from django.contrib.auth.models import User


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
        DOACAO = 5, 'Doação'

    id_venda = models.AutoField(primary_key=True, unique=True)
    id_vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_venda = models.DateField(null=False, blank=False, default=dateNow())
    forma_pagamento = models.IntegerField(null=False, blank=False, default=1)
    ativo = models.BooleanField(default=True)


class ItensVenda(models.Model):
    id_venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    quantidade = models.IntegerField(null=False, blank=False)