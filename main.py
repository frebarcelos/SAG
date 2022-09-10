
import random
class personagem:
    def __init__(self, nome):
        self._pontosDeVida = 100;
        self._nome = nome;
        self._forca = 0;
        self._const = 0;
        self._tam = 0;
        self._des = 0;
        self._apa = 0;
        self._int = 0;
        self._pod = 0;
        self._edu = 0;
        self._mov = 0;

    def personagemNome (self):
        nome = self._nome
        return nome

    def verificaForca (self):
        forca = self._forca
        return forca

    def addForca (self, pontos):
        self.forca += pontos

    def subForca (self, pontos):
        self._forca -= pontos
        return print("Você perdeu {} de pontos de Força".format(pontos))

    def verificaPontosdeVida (self):
        ponto = self._pontosDeVida
        return  ponto
    def addPontosDeVida (self, pontos):
        self._pontosDeVida += pontos

    def subPontosDeVida (self, pontos):
        self._pontosDeVida -= pontos
        print("Seus pontos de vida restante são: {}".format(self.verificaPontosdeVida()))

    def morreu (self):
        if self.verificaPontosdeVida() > 0 :
            return False
        else:
            print("Você Morreu")
            return True
    def testeDeForca (self):
       teste = random.randint(1,101)
       forca = self.verificaForca()
       vida = self.verificaPontosdeVida()
       if forca < teste:
           print("Você falhou no teste")
           vida = int((vida/3))
           personagem.subPontosDeVida(vida)
       else: print("Você Passou no teste")

variavel = 0

while variavel == 0:
    nome = ""
    input("Pressione enter para começar ")
    while nome == "":
        nome: str = input("Digite seu nome:  ")
        if nome == "":
            print("Nome inválido")
    personagem = personagem(nome)
    input("Olá {} vamos começar criando seu personagem".format(personagem.personagemNome()))
    input("Começaremos Distribuindo seus pontos de habilidade")
    input("Seus pontos de Habilidade são divididos em 9 categorias")
    input("Força, Constituição, Tamanho, Destresa, Aparencia, Inteligencia, Poder e Educação")
    resposta = input ("Gostaria de saber mais sobre alguma dessas categorias ? (S/N): ")
    if resposta == "S":
        referencia = 0
        while referencia < 9:
            print("Qual categoria vc gostaria de saber ?  (1) Força, (2) Constituição, (3) Tamanho, (4) Destresa, (5) Aparencia, (6) Inteligencia, (7) Poder  (8) Educação (9) Sair ")
            referencia = int(input())
            if referencia == 1:
                input("Força: mede o poder muscular.")
                input("É usada para julgar o quanto se pode levantar, puxar ou empurrar, ou o quão firme pode-se segurar alguma coisa.")
                input("Também é utilizada para calcular o dano em um combate corpo-a-corpo. ")
                input("Se sua força for reduzida a 0, você se tornará um inválido incapaz de se levantar da cama.")
            elif referencia == 2:
                input("Constituição: ")



    input("Presione enter para começar a história")
    while personagem.verificaPontosdeVida() != 0:
        input("A noite parece começar calma, embora as semanas chuvosas que deixam o clima úmido e pegajoso")
        input(
            "{} vai para a aula com a cabeça abaixada tentando se desviar da fraca chuva que cai sobre a cidade".format(
                personagem.personagemNome()))
        input("sua jaqueta já se encontra parcialmente encharcada e seus tênis além de água também possuem barro. ")
        input("{}:  -Isso que estou apenas indo, imagina depois dessa aula chata".format(personagem.personagemNome()))
        input("seus pontos de vida são: {}".format(personagem.verificaPontosdeVida()))
        personagem.testeDeForca()
        if personagem.morreu(): break

    texto = input("Recomeçar? S/N: ")
    if texto == "S":
        variavel = 0
    else: variavel = 1

print("Bem Jogado !!")
