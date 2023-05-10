from ..models import Professor

# funções de professor

def cadastrar_professor(professor):

    Professor.objects.create(
        nome = professor.nome,
        senha = professor.senha,
        confirmarSenha = professor.confirmarSenha
    )