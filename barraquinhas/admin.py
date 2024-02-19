from django.contrib import admin
from .models import Produtos
from django.contrib.auth.models import User

class CustomAdminSite(admin.AdminSite):
    site_header = 'Administração Baraquinhas'

class AdminProdutos(admin.ModelAdmin):
    list_display = ('nome', 'valor_formatado', 'categoria', 'ativo')
    search_fields = ['nome']

    def valor_formatado(self, obj):
        valor = "R${:,.2f}".format(obj.valor)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    
    valor_formatado.short_description = 'Valor (R$)'

custom_admin_site = CustomAdminSite(name='customadmin')
custom_admin_site.register(User, admin.ModelAdmin)
custom_admin_site.register(Produtos, AdminProdutos)