
from ..models import Endereco


def cadastrar_endereco(endereco):
   return  Endereco.objects.create(rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento,
                           bairro=endereco.bairro, cidade=endereco.cidade,pais=endereco.pais)



def listar_endereco_id(id):
   endereco = Endereco.objects.get(id = id)
   return endereco

def editar_endereco(endereco, endereco_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE enderecos_endereco SET nome={nome} WHERE id=2")
    endereco.rua = endereco_novo.rua
    endereco.numero = endereco_novo.numero
    endereco.complemento = endereco_novo.complemento
    endereco.bairro = endereco_novo.bairro
    endereco.cidade = endereco_novo.cidade
    endereco.pais = endereco_novo.pais
    endereco.save(force_update=True)

def remover_endereco(endereco):
   endereco.delete()