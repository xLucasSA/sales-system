# Generated by Django 4.2.10 on 2024-06-02 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barraquinhas', '0014_remove_vendas_ativo_alter_vendas_data_venda_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='id_vendedor',
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data_venda',
            field=models.DateField(default=datetime.date(2024, 6, 2)),
        ),
    ]
