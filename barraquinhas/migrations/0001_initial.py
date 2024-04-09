# Generated by Django 4.2.10 on 2024-02-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.IntegerField()),
                ('categoria', models.CharField(choices=[('A', 'Alimentos'), ('B', 'Bebidas'), ('J', 'Jogos'), ('O', 'Outros')], default='O', max_length=1)),
                ('ativo', models.BooleanField()),
                ('medida', models.CharField(choices=[('ml', 'ml'), ('un', 'Unidade'), ('kg', 'Kg'), ('lt', 'Lata'), ('ot', 'Outros')], default='ot', max_length=2)),
            ],
        ),
    ]