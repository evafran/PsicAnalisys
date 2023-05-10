class resposta():
    def __init__(self,Resposta,RespostaMuitoRaramente,RespostaAsVezes,
                    RespostaFrequentemente,RespostaSempre,questionario):
        self.__Resposta = Resposta
        self.__RespostaMuitoRaramente = RespostaMuitoRaramente
        self.__RespostaAsVezes = RespostaAsVezes
        self.__RespostaFrequentemente = RespostaFrequentemente
        self.__RespostaSempre = RespostaSempre
        self.__questionario = questionario
    

    @property
    def Resposta(self):
        return self.__Resposta

    @Resposta.setter
    def Resposta(self, Resposta):
        self.__Resposta = Resposta

    @property
    def RespostaMuitoRaramente(self):
        return self.__RespostaMuitoRaramente

    @RespostaMuitoRaramente.setter
    def RespostaMuitoRaramente(self, RespostaMuitoRaramente):
        self.__RespostaMuitoRaramente = RespostaMuitoRaramente


    @property
    def RespostaAsVezes(self):
        return self.__RespostaAsVezes

    @RespostaAsVezes.setter
    def RespostaAsVezes(self, RespostaAsVezes):
        self.__RespostaAsVezes = RespostaAsVezes


    @property
    def RespostaFrequentemente(self):
        return self.__RespostaFrequentemente

    @RespostaFrequentemente.setter
    def RespostaFrequentemente(self, RespostaFrequentemente):
        self.__RespostaFrequentemente = RespostaFrequentemente
    
    @property
    def RespostaSempre(self):
        return self.__RespostaSempre

    @RespostaSempre.setter
    def RespostaSempre(self, RespostaSempre):
        self.__RespostaSempre = RespostaSempre

    @property
    def __questionario(self):
        return self.____questionario

    @__questionario.setter
    def __questionario(self, __questionario):
        self.____questionario = __questionario

    