from ..models import Questionario



def cadastrar_Pergunta(questionario):
    Questionario.objects.create(
        pergunta = questionario.pergunta,
        tipo = questionario.tipo,
        usuario = questionario.usuario
    )

def listar_perguntas():
     return Questionario.objects.all()

    # return Tarefa.objects.filter(usuario = usuario).all()