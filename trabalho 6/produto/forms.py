from django import forms
from django.core.validators import RegexValidator

from produto.models import Produto, Categoria


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('categoria', 'nome', 'quantidade','preco')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages = {'required': 'Campo obrigatório.',
                                              'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-md'})


        self.fields['categoria'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset = Categoria.objects.all().order_by('id')
        self.fields['categoria'].empty_label = '--- Selecione uma categoria ---'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['preco'].min_value = 0
        self.fields['preco'].error_messages = {'required': 'Campo obrigatório.',
                                               'invalid': 'Valor inválido.',
                                               'max_digits': 'Mais de 5 dígitos no total.',
                                               'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                               'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['quantidade'].min_value=0
        self.fields['quantidade'].error_messages={
            'required': 'Campo obrigatório',
            'min_value': 'A quantidade deve ser maior ou igual a zero.'
        }
        self.fields['quantidade'].widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })


class QuantidadeForm(forms.Form):

    produto_id = forms.CharField(widget=forms.HiddenInput())


    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control btn-secondary quantidade',
                                      'style': 'text-align: center; background-color: #6c757d; width: 70px;',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)',
                                      'readonly': 'readonly'}),
        required=True
    )
