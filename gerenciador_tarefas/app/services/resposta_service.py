from ..models import Resposta



def cadastrar_Resposta(resposta):
    Resposta.objects.create(
        Resposta = resposta.Resposta,
        RespostaMuitoRaramente = resposta.RespostaMuitoRaramente,
        RespostaAsVezes = resposta.RespostaAsVezes,
        RespostaFrequentemente = resposta.RespostaFrequentemente,
        RespostaSempre = resposta.RespostaSempre,
        questionario = resposta.questionario
    
    )

def listar_resposta():
     return Resposta.objects.all()