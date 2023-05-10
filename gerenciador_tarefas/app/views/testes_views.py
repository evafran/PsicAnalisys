from django.shortcuts import render,redirect,HttpResponse
from ..forms import PerguntaForm
from django.contrib.auth.decorators import login_required
from ..entidades.questionario import questionario
from ..services import questionario_service


def ego2(request):
    return render(request,'testes/estados_dos_egos2.html')

@login_required()
def listar_perguntas(request):
    questionario = questionario_service.listar_perguntas()
    return render(request,'testes/estados_dos_egos.html',{"questionario":questionario})

@login_required()
def adicionar_pergunta(request):
    perguntaForm = PerguntaForm()
    if request.method == "POST":
        perguntaForm = PerguntaForm(request.POST)
        if perguntaForm.is_valid():
            pergunta = perguntaForm.cleaned_data["pergunta"]
            tipo = perguntaForm.cleaned_data["tipo"]           
            pergunta_nova = questionario(pergunta=pergunta,tipo=tipo,usuario=request.user)
            questionario_service.cadastrar_Pergunta(pergunta_nova)
            return HttpResponse('-------Deu certo-------')
        else:
            perguntaForm = PerguntaForm()
    return render(request,'testes/form_teste.html',{"perguntaForm":perguntaForm})


