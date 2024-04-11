from django import forms
from .models import Vendas, ItensVenda

class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = '__all__'

class FormaPagamento(VendasForm):
    class Meta:
        model = Vendas
        fields = ['forma_pagamento']
        labels = {
            'forma_pagamento': 'Forma de Pagamento'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'
            self.fields[campo].widget.attrs['placeholder'] = campo
            self.fields[campo].widget.attrs['name'] = campo

class ItensVendasForm(forms.ModelForm):
    class Meta:
        model = ItensVenda
        fields = '__all__'
