from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from produto.models import Categoria, Produto


def cardapio(request):
    lista_categorias = Categoria.objects.all().order_by('id')
    lista_produtos = []
    iterator = 0
    for i in lista_categorias:
        lista_produtos.append([])
        lista_produtos[iterator] = [i, Produto.objects.filter(disponivel=True, categoria=i.id).order_by('nome')]
        paginator = Paginator(lista_produtos[iterator][1], 4)
        pagina = request.GET.get(i.slug)
        page_obj = paginator.get_page(pagina)
        lista_produtos[iterator][1] = page_obj
        iterator = iterator + 1


    print("page obj:")
    print(page_obj)

    return render(request, 'produto/cardapio.html', {'categorias_produtos': lista_produtos})