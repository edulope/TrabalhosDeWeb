from django.shortcuts import render

# Create your views here.
from produto.models import Produto


def carrinho(request):
    carrinho = []
    item1 = Produto.objects.get(id=1)
    item2 = Produto.objects.get(id=2)
    item3 = Produto.objects.get(id=3)
    carrinho.append([item1, 2])
    carrinho.append([item2, 1])
    carrinho.append([item3, 3])
    preco = 0
    for i in carrinho:
        preco = preco + i[0].preco * i[1]
    print(carrinho)
    print(preco)
    return render(request, 'carrinho/finalizacao.html', {'itens': carrinho,
                                                        'preco': preco})