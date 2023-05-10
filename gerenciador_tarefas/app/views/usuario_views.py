from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/listar_tarefas')
    else:
        form_usuario = UserCreationForm()
    return render(request,'usuarios/form_usuario.html',{"form_usuario":form_usuario})


def logar_usuario(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # Chave = request.POST["chave"]
        # if Chave == "EricBerne":
        usuario = authenticate(request,username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/listar_tarefas')
        else:
            messages.error(request, 'Vocẽ digitou algo de errado')
            return redirect('/logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html',{"form_login":form_login})



def deslogar(request):
 logout(request)
 return redirect('/logar_usuario')