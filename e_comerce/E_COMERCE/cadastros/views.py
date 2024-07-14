from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import produto,Compra_campo
from .forms import Formulario

class Venda(CreateView):
    model=produto
    fields=['tipo','nome','preco','promocao']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('inicio')

class EditarVenda(UpdateView):
    model=produto
    fields=['tipo','nome','preco','promocao']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('inicio')

class ListarVendas(ListView):
    model=produto
    template_name='cadastros/listar_vendas.html'

class DeletarVenda(DeleteView):
    model=produto
    template_name='cadastros/excluir_venda.html'
    success_url=reverse_lazy('inicio')

class Compra(CreateView):
    model=Compra_campo
    fields=['compra']
    template_name='cadastros/comprar.html'
    success_url=reverse_lazy('inicio')

class ListarCompra(ListView):
    model=Compra_campo
    template_name='cadastros/listar_compras.html'

class EditarCompra(UpdateView):
    model=Compra_campo
    fields=['compra.tipo','compra.nome','compra.preco']
    template_name='cadastros/EditarCompra.html'
    success_url=reverse_lazy('inicio')

class ExcluirCompra(DeleteView):
    model=Compra_campo
    template_name='cadastros/ExcluirCompra.html'
    success_url=reverse_lazy('inicio')