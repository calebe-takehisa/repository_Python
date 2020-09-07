class Calculadora:
    __area_teto: float
    __area_paredes: float

    def calcular_area_paredes(self, comodo):
        self.__area_paredes: float = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

    def calcular_area_teto(self, comodo):
        self.__area_teto: float = comodo.largura * comodo.profundidade
        return self.__area_teto

    def calcular_litragem_necessaria(self):
        if self.__area_paredes <= 0 or self.__area_teto <= 0:
            print(
                'Não é possível calcular a litragem com os valores informados'
            )
            exit()
        litragem_necessaria: float = (self.__area_paredes + self.__area_teto) / 10
        return litragem_necessaria
