from django.shortcuts import render

from produto.forms import ProdutoForm, QuantidadeForm
from produto.models import Produto, Categoria
from django.core.signing import Signer


signer = Signer()


def index(request):
    produtoForm = ProdutoForm()
    lista_produtos = Produto.objects.all().order_by('id')
    lista_forms = []
    total = 0
    for i in lista_produtos:
        total = total + i.preco*i.quantidade
        lista_forms.append(QuantidadeForm(
            initial={'quantidade': i.quantidade,
                     'produto_id': signer.sign(i.id)}
        ))

    ids = []
    lista_categorias = Categoria.objects.all().order_by('id')
    for i in lista_categorias:
        ids.append(i.id)

    return render(request, 'index.html',{'form': produtoForm, 'categoriasZip': zip(ids, lista_categorias), 'produtos': zip(lista_produtos, lista_forms), 'total': total})

def atualiza_tabela(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        id = signer.unsign(form.cleaned_data['produto_id'])
        quantidade = form.cleaned_data['quantidade']

        instance = Produto.objects.get(id=id)


        if (quantidade == 0):
            instance.delete()
        else:
            instance.quantidade = quantidade
            instance.save()

        total = 0
        lista_produtos = Produto.objects.all().order_by('id')
        for i in lista_produtos: total = total + i.preco * i.quantidade


        return render(request, 'resposta_update.html', {
            'total': total
        })
    else:
        raise ValueError('Ocorreu um erro inesperado.')



def cria_elemento(request):
    form = ProdutoForm(request.POST)

    if form.is_valid():
        p = Produto()
        p.nome = form.cleaned_data['nome']
        p.categoria = form.cleaned_data['categoria']
        p.preco = form.cleaned_data['preco']
        p.quantidade = form.cleaned_data['quantidade']
        p.save()

        f = QuantidadeForm(
            initial={'quantidade': p.quantidade,
                     'produto_id': signer.sign(p.id)}
        )

        total = 0
        lista_produtos = Produto.objects.all().order_by('id')
        for i in lista_produtos: total = total + i.preco * i.quantidade

        return render(request, 'resposta_create.html', {
            'produto': p,
            'form': f,
            'total': total
        })
    else:
        raise ValueError('Ocorreu um erro inesperado.')




def deleta_elemento(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        id = signer.unsign(form.cleaned_data['produto_id'])
        instance = Produto.objects.get(id=id)
        instance.delete()

        total = 0
        lista_produtos = Produto.objects.all().order_by('id')
        for i in lista_produtos: total = total + i.preco * i.quantidade

        return render(request, 'resposta_delete.html', {
            'total': total
        })
    else:
        raise ValueError('Ocorreu um erro inesperado.')