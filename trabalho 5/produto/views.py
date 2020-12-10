from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.defaultfilters import slugify
from django.urls import reverse
from produto.models import Produto as Prod, Categoria

from produto.forms import ProdutoForm

from produto.forms import CategoriaForm

from produto.forms import PesquisaForm


def cardapio(request):
    lista_categorias = Categoria.objects.all().order_by('id')
    lista_produtos = []
    iterator = 0
    for i in lista_categorias:
        lista_produtos.append([])
        lista_produtos[iterator] = [i, Prod.objects.filter(disponivel=True, categoria=i.id).order_by('nome')]
        paginator = Paginator(lista_produtos[iterator][1], 4)
        pagina = request.GET.get(i.slug)
        page_obj = paginator.get_page(pagina)
        lista_produtos[iterator][1] = page_obj
        iterator = iterator + 1


    print("page obj:")
    print(page_obj)

    return render(request, 'produto/cardapio.html', {'categorias_produtos': lista_produtos})


def editar(request):
    form = PesquisaForm(request.GET)

    if(form.is_valid()):
        nome = form.cleaned_data['pesquisa']
        lista_produtos = Prod.objects.filter(nome__icontains=nome).order_by('nome')
        lista_categorias = Categoria.objects.filter(nome__icontains=nome).order_by('id')
        paginator = Paginator(lista_produtos, 4)
        pagina = request.GET.get('pagina')
        produtos = paginator.get_page(pagina)
        falha = False

        if request.POST:
            categoriaForm = CategoriaForm(request.POST)

            if categoriaForm.is_valid():
                categoria = categoriaForm.save(commit=False)
                categoria.slug = slugify(categoria.nome)
                categoria.save()

                return redirect('produto:editar')
            else:
                falha = True
        else:
            categoriaForm = CategoriaForm()


        return render(request, 'produto/edicao.html', {'produtos': produtos, 'categorias': lista_categorias, 'form': categoriaForm, 'falha': falha, 'formPesquisa': form, 'nome': nome})



def cadastrar_produtos(request):
    id = None
    if request.POST:
        produto_id = request.session.get('produto_id')
        if produto_id:
            produto = get_object_or_404(Prod, id=produto_id)
            produtoForm = ProdutoForm(request.POST, request.FILES, instance=produto)
            id = produto.id

        else:
            produtoForm = ProdutoForm(request.POST, request.FILES)

        if produtoForm.is_valid():
            Produto = produtoForm.save(commit=False)
            Produto.slug = slugify(Produto.nome)
            Produto.save()
            if produto_id:
                del request.session['produto_id']

            return redirect('produto:editar')
    else:
        try:
            del request.session['produto_id']
        except KeyError:
            pass
        produtoForm = ProdutoForm()
    return render(request, 'produto/cadastro_produtos.html', {'form':produtoForm, 'id': id})





def edita_produto(request, id):
    produto = get_object_or_404(Prod, id=id)
    produto_form = ProdutoForm(instance=produto)
    request.session['produto_id'] = int(id)
    return render(request, 'produto/cadastro_produtos.html', {'form': produto_form, 'id': id})

def remove_produto(request, id):
    produto = get_object_or_404(Prod, id=id)
    produto.imagem.delete()
    produto.delete()
    return redirect('produto:editar')


def remove_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('produto:editar')