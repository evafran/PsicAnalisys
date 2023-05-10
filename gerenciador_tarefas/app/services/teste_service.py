from ..models import Testes



def cadastrar_Aluno_Teste(teste):
    Testes.objects.create(  
        nome = teste.nome, 
        aluno = teste.aluno, 
    )

def listar_usuarios(usuario):
    return Testes.objects.filter(usuario = usuario).all()

def listar_Testes_id(id):
    return Testes.objects.get(id = id)