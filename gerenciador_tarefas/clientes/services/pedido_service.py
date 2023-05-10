
from ..models import Pedidos
from .produto_service import *

from django.db import connection

def cadastrar_pedido(pedido):
    pedido_bd = Pedidos.objects.create(cliente = pedido.cliente,
     data_pedido = pedido.data_pedido,
    valor= pedido.valor, status = pedido.status,
    observacoes = pedido.observacoes)
    pedido_bd.save()
    for i in pedido.produtos:
        produto = listar_produto_id(i.id)
        pedido_bd.produtos.add(produto)



def listar_pedidos():
    # pedidos = Pedidos.objects.all() para evitar o problema 
    # do django n + 1, é utilizado para relacionamentos 1 para n ou 1 para 1 temos que fazer INNER JOIN poi assim o django faz as relações diretemente proporcionais a quantidade de pedidos e clientes a linha de baixo é o que se deve fazer
    # para relacionamentos n para n temos que usar o .prefetch_related('nome').all()
    # pedidos = Pedidos.objects.select_related('cliente').all()
    pedidos = Pedidos.objects.prefetch_related('produtos').all()
    # for i in pedidos:
    #     print(i.produtos.all())
    # print(connection.queries)
    # print(len(connection.queries))
    return pedidos

def listar_pedido_id(id):
    pedido = Pedidos.objects.get(id=id)
    return pedido


def editar_pedido(pedido, pedido_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE pedidos_pedido SET nome={nome} WHERE id=2")
    pedido.cliente = pedido_novo.cliente
    pedido.observacoes = pedido_novo.observacoes
    pedido.data_pedido = pedido_novo.data_pedido
    pedido.valor = pedido_novo.valor
    pedido.status = pedido_novo.status
    pedido.produtos.set(pedido_novo.produtos)
    pedido.save(force_update=True)


def remover_pedido(pedido):
   pedido.delete()