
class personagem:

    def __init__(self, nome):
        self.__pontosDeVida = 0;
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
        self.__san = 0;

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
        return print("Você ganhou {0} de pontos de Força! \nSua Forca agora é {1} ".format(pontos, self.forca))

    def subForca(self, pontos):
        self.__forca -= pontos
        return print("Você perdeu {0} de pontos de Força! \nSua Forca agora é {1} ".format(pontos, self.forca))

    @property
    def const(self):
        const = self.__const
        return const
    def addConst(self, pontos):
        self.__const += pontos
        return print \
            ("Você ganhou {0} de pontos de Constituição! \nSua Constituição agora é {1} ".format(pontos, self.const))

    def subConst(self, pontos):
        self.__const -= pontos
        return print \
            ("Você perdeu {0} de pontos de Constituição! \nSua Constituição agora é {1} ".format(pontos, self.const))

    @property
    def tam(self):
        tam = self.__tam
        return tam

    def addTam(self, pontos):
        self.__tam += pontos
        return print(
            "Você ganhou {0} de pontos de Tamanho! \nSeu Tamanho agora é {1} ".format(pontos, self.tam))

    def subTam(self, pontos):
        self.__tam -= pontos
        return print(
            "Você perdeu {0} de pontos de Tamanho! \nSeu Tamanho agora é {1} ".format(pontos, self.tam))

    @property
    def des(self):
        ponto = self.__des
        return ponto

    def addDes(self, pontos):
        self.__des += pontos
        return print(
            "Você ganhou {0} de pontos de Destreza! \nSua Destreza agora é {1} ".format(pontos, self.des))

    def subDes(self, pontos):
        self.__des -= pontos
        return print(
            "Você perdeu {0} de pontos de Destreza! \nSua Destreza agora é {1} ".format(pontos, self.des))

    @property
    def apa(self):
        ponto = self.__apa
        return ponto

    def addApa(self, pontos):
        self.__apa += pontos
        return print(
            "Você ganhou {0} de pontos de Aparencia! \nSua Aparencia agora é {1} ".format(pontos, self.apa))

    def subApa(self, pontos):
        self.__apa -= pontos
        return print(
            "Você perdeu {0} de pontos de Aparencia! \nSua Aparencia agora é {1} ".format(pontos, self.apa))

    @property
    def int(self):
        ponto = self.__int
        return ponto

    def addInt(self, pontos):
        self.__int += pontos
        return print(
            "Você ganhou {0} de pontos de Inteligência! \nSua Inteligência agora é {1} ".format(pontos, self.int))

    def subInt(self, pontos):
        self.__des -= pontos
        return print(
            "Você perdeu {0} de pontos de Inteligência! \nSua Inteligência agora é {1} ".format(pontos, self.int))

    @property
    def pod(self):
        ponto = self.__pod
        return ponto

    def addPod(self, pontos):
        self.__pod += pontos
        return print(
            "Você ganhou {0} de pontos de Poder! \nSeu Poder agora é {1} ".format(pontos, self.pod))

    def subPod(self, pontos):
        self.__des -= pontos
        return print(
            "Você perdeu {0} de pontos de Poder! \nSeu Poder agora é {1} ".format(pontos, self.pod))

    @property
    def edu(self):
        ponto = self.__edu
        return ponto

    def addEdu(self, pontos):
        self.__edu += pontos
        return print(
            "Você ganhou {0} de pontos de Educação! \n Sua Educação agora é {1} ".format(pontos, self.edu))

    def subEdu(self, pontos):
        self.__edu -= pontos
        return print(
            "Você perdeu {0} de pontos de Educação! \n Sua Educação agora é {1} ".format(pontos, self.edu))

    @property
    def pontosDeVida(self):
        pontos = self.__pontosDeVida
        return pontos

    def CalculaPontosDeVida(self):
        pontos = int((self.__const + self.__tam ) /2)
        self.__pontosDeVida = pontos
        return print("Você tem {} de pontos de Vida".format(self.pontosDeVida))

    def addPontosDeVida(self, pontos):
        self.__pontosDeVida += pontos
        return print("Você ganhou {0} de pontos de Pontos de Vida!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.pontosDeVida))

    def subPontosDeVida(self, pontos):
        self.__pontosDeVida -= pontos
        return print("Você ganhou {0} de pontos de Pontos de Vida!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.pontosDeVida))


    @property
    def san(self):
        pontos = self.__san
        return pontos
    def CalculaSanidade(self):
        pontos = (self.pod * 5)
        self.__san = pontos
        return print("Você tem {} de Sanidade".format(self.san))

    def addPontosSanidade(self, pontos):
        if self.san < 100:
         self.__san += pontos
         print("Você ganhou {0} de pontos de Sanidade!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.san))
        else: print("Você tem os pontos maximos de sanidade")

    def subPontosSanidade(self, pontos):
        self.__san -= pontos
        return print("Você ganhou {0} de pontos de Sanidade!! \n Seus Pontos de Vida agora são {1} ".format(pontos, self.san))

    def morreu(self):
        if self.pontosDeVida > 0:
            return False
        else:
            print("Seus pontos de vida chegaram a 0 \nVocê Morreu")
            return True
    def doido(self):
        if self.san > 0:
            return False
        else:
            print("Seus pontos de Sanidade chegaram a 0 \nVocê não mais controla seus sentidos")
            return True
