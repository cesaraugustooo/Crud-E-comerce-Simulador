from django.urls import path
from .views import Venda,EditarVenda,ListarVendas,DeletarVenda,Compra,ListarCompra,EditarCompra,ExcluirCompra


urlpatterns =[
    path("venda",Venda.as_view(),name='venda'),
    path("editar/venda/<int:pk>",EditarVenda.as_view(),name='editar-venda'),
    path("listar/vendas",ListarVendas.as_view(),name='listar-venda'),
    path("excluir/vendas/<int:pk>",DeletarVenda.as_view(),name='excluir-venda'),
    path('comprar',Compra.as_view(),name='compra'),
    path("listar/comprass",ListarCompra.as_view(),name='listar-compra'),
    path("editarr/comprass/<int:pk>",EditarCompra.as_view(),name='editar-compra'),
    path("excluir/comprass/<int:pk>",ExcluirCompra.as_view(),name='excluir-compra')
    
]
