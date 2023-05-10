from django.shortcuts import render,redirect,HttpResponse
from ..forms import TarefaForm
from django.contrib.auth.decorators import login_required
from ..entidades.tarefa import tarefa
from ..services import tarefa_service
# from ..services import aluno_service
# from ..models import Aluno
from ..models import Tarefa
from rest_framework import generics
from ..serializers import AlunoSerializer
from ..serializers import TarefaSerializer

# Create your views here.

class ListAlunos(generics.ListCreateAPIView):

    # queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ListTarefas(generics.ListCreateAPIView):

    queryset = Tarefa.objects.all()
    serializer_class =TarefaSerializer


def home(request):
    return render(request,'tarefas/form_tarefa.html')

def teste(request):
    return render(request,'testes/FormEstEgo.html')

def ego(request):
    aluno = aluno_service.id_aluno(request.user)
    return render(request,'testes/estados_dos_egos.html',{"aluno":aluno})

@login_required()
def listar_tarefas(request):

    tarefas = tarefa_service.listar_tarefas(request.user)

    # alunos = Aluno.objects.all()
    

    context = {
        # 'alunos': alunos,
        'tarefas': tarefas,
    }

    return render(request,'tarefas/listar_tarefas.html',context)


@login_required()
def cadastrar_tarefa(request):

    form_tarefa = TarefaForm()
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            titulo = form_tarefa.cleaned_data["titulo"]
            descricao = form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]
            tarefa_nova = tarefa(titulo=titulo,descricao=descricao,data_expiracao=data_expiracao,
            prioridade=prioridade,usuario=request.user)
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect('/listar_tarefas')
        else:
            form_tarefa = TarefaForm()


    return render(request,'tarefas/form_tarefa.html', {"form_tarefa":form_tarefa})

@login_required()

def editar_tarefa(request,id):
    tarefa_bd = tarefa_service.listar_tarefa_id(id) 
    if tarefa_bd != request.user:
        return HttpResponse("Não permitido")  
    form_tarefa = TarefaForm(request.POST or None ,instance=tarefa_bd)
    if form_tarefa.is_valid():
         titulo = form_tarefa.cleaned_data["titulo"]
         descricao = form_tarefa.cleaned_data["descricao"]
         data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
         prioridade = form_tarefa.cleaned_data["prioridade"]
         tarefa_nova = tarefa(titulo=titulo,descricao=descricao,data_expiracao=data_expiracao,
         prioridade=prioridade,usuario = request.user)
         tarefa_service.editar_tarefa(tarefa_bd,tarefa_nova)
    return render(request,'tarefas/form_tarefa.html',{"form_tarefa":form_tarefa})

@login_required()
def remover_tarefa(request,id):

    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    if tarefa_bd != request.user:
        return HttpResponse("Não permitido")  
    if request.method == "POST":
        tarefa_service.remover_tarefa(tarefa_bd)
        return redirect('/listar_tarefas')
    return render(request,'tarefas/confirma_exclusao.html',{"tarefa":tarefa_bd})
    