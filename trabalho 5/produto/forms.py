from django import forms
from django.core.validators import RegexValidator

from produto.models import Produto, Categoria




class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('categoria', 'nome', 'descricao','imagem','preco','disponivel')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages = {'required': 'Campo obrigatório.',
                                              'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-md'})

        self.fields['descricao'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})

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

        self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        self.fields['imagem'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})
        self.fields['imagem'].required = True


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nome',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages = {'required': 'Campo obrigatório.',
                                              'unique': 'Nome de Categoria duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-md'})


class PesquisaForm(forms.Form):

    pesquisa = forms.CharField(
        widget=forms.TextInput( attrs={'placeholder': 'Pesquisa por nome', 'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False)
