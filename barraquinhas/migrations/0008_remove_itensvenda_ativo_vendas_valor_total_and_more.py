# Generated by Django 4.2.10 on 2024-04-10 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barraquinhas', '0007_alter_produtos_ativo_alter_produtos_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itensvenda',
            name='ativo',
        ),
        migrations.AddField(
            model_name='vendas',
            name='valor_total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data_venda',
            field=models.DateField(default=datetime.datetime(2024, 4, 10, 21, 43, 52, 820846, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='forma_pagamento',
            field=models.IntegerField(choices=[(1, 'Dinheiro'), (2, 'Catão de Débito'), (3, 'Cartão de Crédito'), (4, 'PIX')], default=1),
        ),
    ]
