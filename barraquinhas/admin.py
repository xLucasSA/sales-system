from django.contrib import admin
from .models import Produtos, Vendas
from django.contrib.auth.models import User
import datetime

class CustomAdminSite(admin.AdminSite):
    site_header = 'Administração Baraquinhas'

class AdminProdutos(admin.ModelAdmin):
    list_display = ('nome', 'valor_formatado', 'categoria', 'ativo')
    search_fields = ['nome']

    def valor_formatado(self, obj):
        valor = "R$ {:,.2f}".format(obj.valor)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    valor_formatado.short_description = 'Valor (R$)'


class AdminVendas(admin.ModelAdmin):
    list_display = ('id_venda', 'id_vendedor', 'data_formatada', 'get_forma_pagamento', 'valor_formatado', 'ativo_dispaly')
    list_filter = ['ativo']

    def get_forma_pagamento(self, instance):
        return instance.get_forma_pagamento_display()
    get_forma_pagamento.short_description = 'Forma de Pagamento'

    def valor_formatado(self, obj):
        valor = "R$ {:,.2f}".format(obj.valor_total)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    valor_formatado.short_description = 'Valor (R$)'

    def data_formatada(self, obj):
        data =  datetime.date.strftime(obj.data_venda, "%d/%m/%Y")
        return data
    
    @admin.display(boolean=True)
    def ativo_dispaly(self, obj):
        return obj.ativo 

    ativo_dispaly.short_description = 'Está Ativo?'
        

custom_admin_site = CustomAdminSite(name='customadmin')
custom_admin_site.register(User, admin.ModelAdmin)
custom_admin_site.register(Produtos, AdminProdutos)
custom_admin_site.register(Vendas, AdminVendas)