from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("A", "ALTA"),
        ("N", "NORMAL"),
        ("B", "BAIXA"),
    ]
    titulo = models.CharField('titulo',max_length=30,null=False,blank=False)
    descricao = models.TextField('descrica',max_length=130,null=False,blank=False)
    data_expiracao = models.DateField('data',null=False,blank=False)
    prioridade = models.CharField('prioridade', max_length = 1,choices = PRIORIDADE_CHOICES ,null=False,blank=False)
    usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)



class Professor(models.Model):

    nome = models.CharField('nome',max_length=60,null=False,blank=False)
    senha = models.IntegerField('senha',null=False,blank=False)
    confirmarSenha = models.IntegerField('confirmarSenha',null=False,blank=False)

class Testes(models.Model):

    PRIORIDADE_CHOICES = [
        ("1", "Estados-do-Ego"),
        ("2", "Personalidade"),
    ]
    nome = models.IntegerField('nome',choices = PRIORIDADE_CHOICES ,null=False,blank=False)
    # aluno= models.ForeignKey("Aluno", on_delete=models.CASCADE, related_name='Testes', null=False)

class Resposta(models.Model):

    PRIORIDADE_CHOICES = [
        ("0", "Muito-Raramente"),
        ("1", "As-Vezes"),
        ("2", "Frequentemente"),
        ("3", "Sempre"),
    ]
    Resposta = models.IntegerField('resposta',choices = PRIORIDADE_CHOICES ,null=False,blank=False)

    # questionario = models.ManyToManyField(Questionario)

class Questionario(models.Model):
    
    PRIORIDADE_CHOICES = [
        ("1", "Ego"),
        ("2", "Personalidade"),
    ]

    tipo = models.CharField('tipo', max_length = 1,choices = PRIORIDADE_CHOICES ,null=False,blank=False)
    # pergunta = models.CharField('pergunta',max_length=100,null=False,blank=True)
    # usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    # aluno = models.ForeignKey("Aluno",on_delete=models.CASCADE, related_name='questionario')
    respostas = models.OneToOneField(Resposta, on_delete=models.SET_NULL, null= True)
   

class Disciplina(models.Model):

    nome = models.IntegerField('nome',null=False,blank=False)
    professor = models.ManyToManyField(Professor)



class ComplementoUser(models.Model):
    
    usuario = models.OneToOneField(User,null=True, on_delete=models.CASCADE,related_name='complementoUser')


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title


