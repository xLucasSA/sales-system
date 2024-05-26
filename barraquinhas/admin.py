from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Produtos, Vendas
import datetime

AdminSite.site_header = 'Administração Baraquinhas'
AdminSite.site_title = 'Administração Baraquinhas'

@admin.register(Produtos)
class AdminProdutos(admin.ModelAdmin):
    list_display = ('nome', 'valor_formatado', 'categoria', 'ativo')
    search_fields = ['nome']

    def valor_formatado(self, obj):
        valor = "R$ {:,.2f}".format(obj.valor)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    valor_formatado.short_description = 'Valor (R$)'

@admin.register(Vendas)
class AdminVendas(admin.ModelAdmin):
    list_display = ('id_venda', 'id_vendedor', 'data_formatada', 'get_forma_pagamento', 'valor_formatado')

    def get_forma_pagamento(self, instance):
        return instance.get_forma_pagamento_display()
    get_forma_pagamento.short_description = 'Forma de Pagamento'

    def valor_formatado(self, obj):
        valor = "R$ {:,.2f}".format(obj.valor_total)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    valor_formatado.short_description = 'Valor (R$)'

    def data_formatada(self, obj):
        data = datetime.date.strftime(obj.data_venda, "%d/%m/%Y")
        return data
    data_formatada.short_description = 'Data'
        
admin.site.unregister(User)
admin.site.unregister(Group)     