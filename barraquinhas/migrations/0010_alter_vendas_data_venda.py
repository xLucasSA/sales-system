# Generated by Django 4.2.10 on 2024-04-14 01:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barraquinhas', '0009_alter_vendas_options_alter_vendas_data_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data_venda',
            field=models.DateField(default=datetime.datetime(2024, 4, 14, 1, 33, 14, 467160, tzinfo=datetime.timezone.utc)),
        ),
    ]