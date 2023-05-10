class questionario():
    def __init__(self,pergunta,tipo,usuario):
        self.__pergunta = pergunta
        self.__tipo = tipo
        self.__usuario = usuario
    

    @property
    def pergunta(self):
        return self.__pergunta

    @pergunta.setter
    def pergunta(self, pergunta):
        self.__pergunta = pergunta

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    