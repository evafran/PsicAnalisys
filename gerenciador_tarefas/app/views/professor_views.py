
from django.shortcuts import render,redirect,HttpResponse
from ..forms import ProfessorForm
from ..services import professor_service


def cadastrar_professor(request):
    form_professor = ProfessorForm()

    if request.method == "POST":
        form_professor = ProfessorForm(request.POST)

        if form_professor.is_valid():
            nome = form_aluno.cleaned_data["nome"]
            senha = form_aluno.cleaned_data["senha"]
            confirmarSenha = form_aluno.cleaned_data["confirmarSenha"]
            novo_professor = professor(nome=nome,senha=senha,confirmarSenha=confirmarSenha)
            professor_service.cadastrar_professor(novo_professor)
            return render(request,'testes/FormEstEgo.html',{"novo_professor":novo_professor})
        else:
            form_professor = ProfessorForm()

    return render(request,'Professor/cadastrar_professor.html', {"form_professor":form_professor})
