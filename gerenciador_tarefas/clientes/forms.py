from django import forms
from .models import Cliente,Endereco,Pedidos,Produto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sobrenome', 'sexo', 'data_nascimento', 'email', 'profissao']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua','numero','complemento','bairro','cidade','pais']


class PedidoForm(forms.ModelForm):
    class Meta:
        # relacionamento 1 para N
        # cliente = forms.ModelChoiceField(queryset= Cliente.objects.all())
        # # relacionamento N para N
        # produtos = forms.ModelMultipleChoiceField(queryset = Produto.objects.all())
        model = Pedidos
        fields = ['cliente', 'observacoes','data_pedido','valor','status','produtos']


class ProdutoForm(forms.ModelForm):
    class Meta: 
        model = Produto
        fields = ['nome','descricao','valor']
