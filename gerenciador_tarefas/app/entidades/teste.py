class teste():
    def __init__(self,nome,aluno):
        self.__nome = nome
        self.__aluno = aluno

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno