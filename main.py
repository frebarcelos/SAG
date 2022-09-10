class personagem:
    def __init__(self, pontosDeVida, nome):
        self.pontosDeVida = pontosDeVida;
        self.nome = nome;

    def morreu (self):
        if self.pontosDeVida > 0 :
            return False
        else:
            print("Você Morreu")
            return True

variavel = 0
while variavel == 0:
    nome = ""
    pontos = 101
    input("Pressione enter para começar ")
    while nome == "":
        nome: str = input("digite seu nome:  ")
        if nome == "":
            print("Nome inválido")
    while pontos > 100:
        pontos = int(input("digite seus pontos de vida: (1/100) "))
        if pontos > 100:
            print("digite um numero valido")
    personagem = personagem(pontos, nome)
    while personagem.pontosDeVida != 0:
        input("A noite parece começar calma, embora as semanas chuvosas que deixam o clima úmido e pegajoso")
        input(
            "{} vai para a aula com a cabeça abaixada tentando se desviar da fraca chuva que cai sobre a cidade".format(
                personagem.nome))
        input("sua jaqueta já se encontra parcialmente encharcada e seus tênis além de água também possuem barro. ")
        input("{}:  -Isso que estou apenas indo, imagina depois dessa aula chata".format(personagem.nome))
        input("seus pontos de vida são: {}".format(personagem.pontosDeVida))
        personagem.pontosDeVida = 0
        if personagem.morreu() : break

    texto = input("Recomeçar? S/N: ")
    if texto == "S":
        variavel = 0
    else: variavel = 1

print("Bem Jogado !!")
