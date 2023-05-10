

from ..models import Aluno

def cadastrar_aluno(aluno):

    Aluno.objects.create(
        nome = aluno.nome,
        senha = aluno.senha,
        confirmarSenha = aluno.confirmarSenha
    )