from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from .models import *

AdminSite.site_header = 'Administração Baraquinhas'
AdminSite.site_title = 'Administração Baraquinhas'
AdminSite.index_title = ''

@admin.register(Produtos)
class AdminProdutos(admin.ModelAdmin):
    list_display = ('nome', 'valor_formatado', 'categoria', 'ativo', 'imagem_tag')
    search_fields = ['nome']

    def valor_formatado(self, obj):
        valor = "R$ {:,.2f}".format(obj.valor)
        valor = valor.replace('.', '*').replace(',', '.').replace('*', ',')
        return valor
    valor_formatado.short_description = 'Valor (R$)'

    def imagem_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />'.format(obj.imagem.url))
        return "-"
    imagem_tag.short_description = 'Imagem'
        
admin.site.unregister(User)
admin.site.unregister(Group)     