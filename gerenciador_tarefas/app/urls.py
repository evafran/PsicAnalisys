
from django.contrib import admin
from django.urls import path
from . import views
from .views.tarefa_views import *
from .views.usuario_views import *
from .views.testes_views import *
from .views.musica_views import*
from .views.professor_views import*


from django.conf.urls import url





urlpatterns = [
    path('listar_tarefas/', views.tarefa_views.listar_tarefas),
    path('cadastrar_tarefa/', views.tarefa_views.cadastrar_tarefa),
    path('listar_tarefas/editar_tarefa/<int:id>',views.tarefa_views.editar_tarefa , name='editar'),
    path('listar_tarefas/remover_tarefa/<int:id>',views.tarefa_views.remover_tarefa, name= 'remover '),
    path('teste', views.tarefa_views.teste),
    path('ego',views.tarefa_views.ego),
    path('ego2',views.testes_views.ego2),    
    path('cadastrar_usuario/', views.usuario_views.cadastrar_usuario, name ='usuario_Cadastrar'),
    path('logar_usuario/', views.usuario_views.logar_usuario , name= 'logar'),
    path('logout/', views.usuario_views.deslogar , name= 'deslogar'),
    path('cadastrar_perguntas/', views.testes_views.adicionar_pergunta),
    path('listar_perguntas/',views.testes_views.listar_perguntas),
    path('cadastrar_professor/',views.professor_views.cadastrar_professor),
    url(r'^musics/', views.musica_views.MusicList.as_view(), name='music-list'),
    url(r'^listar_alunos/', views.tarefa_views.ListAlunos.as_view(),name='alunos'),
    url(r'^tarefas/',views.tarefa_views.ListTarefas.as_view(), name= 'tarefas'),

]