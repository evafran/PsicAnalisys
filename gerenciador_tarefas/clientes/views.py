from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Cliente
from .forms import ClienteForm
from .forms import PedidoForm
from .forms import EnderecoForm
from .forms import ProdutoForm

from .entidades import cliente,endereco,pedido,produto
from .services import cliente_service,endereco_service,pedido_service,produto_service

from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(20)
def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# @csrf_exempt
# Desativando a proteção CSRF
def inserir_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            sobrenome = form_cliente.cleaned_data["sobrenome"]
            sexo = form_cliente.cleaned_data["sexo"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            email = form_cliente.cleaned_data["email"]
            profissao = form_cliente.cleaned_data["profissao"]
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                numero = form_endereco.cleaned_data["numero"]
                complemento = form_endereco.cleaned_data["complemento"]
                bairro = form_endereco.cleaned_data["bairro"]
                cidade = form_endereco.cleaned_data["cidade"]
                pais = form_endereco.cleaned_data["pais"]
                endereco_novo = endereco.Endereco(rua=rua,numero=numero,complemento=complemento,bairro = bairro,cidade = cidade, pais = pais)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome,sobrenome=sobrenome ,sexo=sexo, data_nascimento=data_nascimento, email=email,
                                           profissao=profissao,endereco= endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar_clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco':form_endereco})

def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})

def editar_cliente(request, id):

    cliente_antigo = cliente_service.listar_cliente_id(id)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_antigo)   

    if cliente_antigo.endereco == None:
        form_endereco = EnderecoForm(request.POST or None)
        # return HttpResponse("entrou")
    else:
        endereco_antigo = endereco_service.listar_endereco_id(cliente_antigo.endereco.id)
        form_endereco = EnderecoForm(request.POST or None, instance = endereco_antigo)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_antigo)   
    if form_cliente.is_valid():

        nome = form_cliente.cleaned_data["nome"]
        sobrenome = form_cliente.cleaned_data["sobrenome"]
        sexo = form_cliente.cleaned_data["sexo"]
        data_nascimento = form_cliente.cleaned_data["data_nascimento"]
        email = form_cliente.cleaned_data["email"]
        profissao = form_cliente.cleaned_data["profissao"] 
        if form_endereco.is_valid:
            rua = request.POST["rua"]
            numero = request.POST["numero"]
            complemento = request.POST["complemento"]
            bairro = request.POST["bairro"]
            cidade = request.POST["cidade"]
            pais = request.POST["pais"]
            endereco_novo = endereco.Endereco(rua=rua,numero=numero,complemento=complemento,bairro = bairro,cidade = cidade, pais = pais)   
            # return HttpResponse("entrou form_endereco")
            if cliente_antigo.endereco == None:
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, email=email,
                                            profissao=profissao,endereco= endereco_bd)
            else:
                endereco_service.editar_endereco(endereco_antigo,endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome,sobrenome = sobrenome, sexo=sexo, data_nascimento=data_nascimento, email=email,
                                                    profissao=profissao, endereco = cliente_antigo.endereco.id)
            cliente_service.editar_cliente(cliente_antigo, cliente_novo)
            return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente,'form_endereco':form_endereco})

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        endereco_service.remover_endereco(endereco)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})



def inserir_pedido(request):
    
    if request.method== "POST":
        form_pedido = PedidoForm(request.POST)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data["cliente"]
            observacoes = form_pedido.cleaned_data["observacoes"]
            valor = form_pedido.cleaned_data["valor"]
            data_pedido = form_pedido.cleaned_data["data_pedido"]
            status = form_pedido.cleaned_data["status"]
            produtos = form_pedido.cleaned_data["produtos"]
            pedido_novo = pedido.Pedido(cliente = cliente, observacoes = observacoes, data_pedido= data_pedido,valor = valor, status = status, produtos=produtos)
            pedido_service.cadastrar_pedido(pedido_novo)
            return redirect('listar_pedidos')
    else:
         form_pedido = PedidoForm()
    return render(request,'pedidos/pedido_forms.html',{'form_pedido':form_pedido})



def listar_pedidos(request):
    pedidos = pedido_service.listar_pedidos()
    return render (request,'pedidos/listar_pedidos.html',{'pedidos':pedidos})



def listar_pedido_id(request, id):
    pedido = pedido_service.listar_pedido_id(id)
    return render(request, 'pedidos/listar_pedido.html', {'pedido': pedido})



def editar_pedido(request, id):

    pedido_antigo = pedido_service.listar_pedido_id(id)
    form_pedido = PedidoForm(request.POST or None, instance=pedido_antigo)   

    # if pedido_antigo == None:
    #     form_endereco = PedidoForm(request.POST or None)
        # return HttpResponse("entrou")
    # else:
    #     endereco_antigo = endereco_service.listar_endereco_id(cliente_antigo.endereco.id)
    #     form_endereco = EnderecoForm(request.POST or None, instance = endereco_antigo)
    # form_cliente = ClienteForm(request.POST or None, instance=cliente_antigo)   
    if form_pedido.is_valid():

        cliente = form_pedido.cleaned_data["cliente"]
        observacoes = form_pedido.cleaned_data["observacoes"]
        data_pedido = form_pedido.cleaned_data["data_pedido"]
        valor = form_pedido.cleaned_data["valor"]
        status = form_pedido.cleaned_data["status"] 
        produtos = form_pedido.cleaned_data["produtos"]
        pedido_novo = pedido.Pedido(cliente = cliente, observacoes=observacoes,
        data_pedido = data_pedido,valor = valor, status = status, produtos= produtos)
        pedido_service.editar_pedido(pedido_antigo,pedido_novo)
        return redirect('/listar_pedidos')
    return render(request, 'pedidos/pedido_forms.html', {'form_pedido': form_pedido})


def remover_pedido(request, id):
    pedido = pedido_service.listar_pedido_id(id)
    # endereco = endereco_service.listar_endereco_id(pedido.endereco.id)
    if request.method == "POST":
        pedido_service.remover_pedido(pedido)
        return redirect('listar_pedidos')
    return render(request, 'pedidos/confirma_exclusao.html', {'pedido': pedido})


def inserir_produto(request):
    
    if request.method== "POST":
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            nome = form_produto.cleaned_data["nome"]
            descricao = form_produto.cleaned_data["descricao"]
            valor = form_produto.cleaned_data["valor"]
            produto_novo = produto.Produto(nome=nome,descricao=descricao,valor=valor)
            produto_service.inserir_produto(produto_novo)
            return redirect('listar_produtos')
    else:
        form_produto = ProdutoForm()
    return render(request, 'produtos/form_produtos.html', {'form_produto': form_produto})


def listar_produtos(request):
    produtos = produto_service.listar_produtos()
    return render (request,'produtos/listar_produtos.html',{'produtos':produtos})

def listar_produto_id(request, id):
    produto = produto_service.listar_produto_id(id)
    return render(request, 'produtos/listar_produto.html', {'produto': produto})