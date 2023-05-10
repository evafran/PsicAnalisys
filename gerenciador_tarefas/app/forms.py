from django import forms
from .models import Tarefa
from .models import Questionario
from .models import Resposta
from .models import Testes
from .models import Professor


class TarefaForm(forms.ModelForm):
    class Meta :
        model = Tarefa
        exclude = ('usuario',)
        fields = '__all__'

class PerguntaForm(forms.ModelForm):
    class Meta :
        model = Questionario
        exclude = ('usuario',)
        fields = '__all__'



class ProfessorForm(forms.ModelForm):

    senha = forms.CharField( widget=forms.PasswordInput)
    confirmarSenha = forms.CharField ( widget = forms.PasswordInput)

    class Meta :
        model = Professor
        fields = '__all__'


class RespostaForm(forms.ModelForm):
    class Meta :
        model = Resposta
        fields = '__all__'

class TesteForm(forms.ModelForm):
    class Meta :
        model = Testes
        fields = '__all__'

