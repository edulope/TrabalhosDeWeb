from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.cardapio, name="cardapio"),
    path('cadastrar_produtos', views.cadastrar_produtos, name="cadastrar_produtos"),
    path('editar', views.editar, name="editar"),
    path('remove_categoria/<int:id>/', views.remove_categoria, name="remove_categoria"),
    #path('editar/<sucesso>/', views.editar, name="editar"),
    #path('exibe_produto/<int:id>/', views.exibe_produto, name='exibe_produto'),
    path('edita_produto/<int:id>/', views.edita_produto, name='edita_produto'),
    path('remove_produto/<int:id>/', views.remove_produto, name="remove_produto"),

]