import random


class personagem:

    def __init__(self, nome):
        self.__pontosDeVida = 100;
        self.__nome = nome;
        self.__forca = 0;
        self.__const = 0;
        self.__tam = 0;
        self.__des = 0;
        self.__apa = 0;
        self.__int = 0;
        self.__pod = 0;
        self.__edu = 0;
        self.__mov = 0;
        self.__san = 100;

    @property
    def nome(self):
        nome = self.__nome
        return nome

    def alteraNome(self, nome):
        self.__nome = nome
        return print(nome)
    @property
    def forca(self):
        forca = self.__forca
        return forca

    def addForca(self, pontos):
        self.__forca += pontos
        return print("Você ganhou {0} de pontos de Força!! \n Sua Forca agora é {1} ".format(pontos, self.forca))

    def subForca(self, pontos):
        self.__forca -= pontos
        return print("Você perdeu {0} de pontos de Força!! \n Sua Forca agora é {1} ".format(pontos, self.forca))

    @property
    def pontosDeVida(self):
        pontos = self.__pontosDeVida
        return pontos

    def CalculaPontosDeVida(self):
        pontos = (self.__const + self.__tam)/2
        return print("Você tem {} de pontos de Vida".format(pontos))

    def addPontosDeVida(self, pontos):
        self.__pontosDeVidaa += pontos
        return print("Você ganhou {0} de pontos de Pontos de Vida!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.pontosDeVida))

    def addPontosDeVida(self, pontos):
        self.__pontosDeVida -= pontos
        return print("Você ganhou {0} de pontos de Pontos de Vida!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.pontosDeVida))



















    def morreu(self):
        if self.verificaPontosdeVida() > 0:
            return False
        else:
            print("Você Morreu")
            return True

