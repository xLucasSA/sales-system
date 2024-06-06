# Generated by Django 4.2.10 on 2024-06-06 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barraquinhas', '0016_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data_venda',
            field=models.DateField(default=datetime.date(2024, 6, 6)),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='forma_pagamento',
            field=models.IntegerField(choices=[(1, 'Dinheiro'), (2, 'Catão de Débito'), (3, 'Cartão de Crédito'), (4, 'PIX'), (5, 'Devolução')], default=1),
        ),
    ]
