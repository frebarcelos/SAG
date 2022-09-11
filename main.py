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

    def personagemNome(self):
        nome = self._nome
        return nome

    def verificaForca(self):
        forca = self._forca
        return forca

    def addForca(self, pontos):
        self.forca += pontos

    def subForca(self, pontos):
        self._forca -= pontos
        return print("Você perdeu {} de pontos de Força".format(pontos))

    def verificaPontosdeVida(self):
        ponto = self._pontosDeVida
        return ponto

    def addPontosDeVida(self, pontos):
        self._pontosDeVida += pontos

    def subPontosDeVida(self, pontos):
        self._pontosDeVida -= pontos
        print("Seus pontos de vida restante são: {}".format(self.verificaPontosdeVida()))

    def morreu(self):
        if self.verificaPontosdeVida() > 0:
            return False
        else:
            print("Você Morreu")
            return True

    def testeDeForca(self):
        teste = random.randint(1, 101)
        forca = self.verificaForca()
        vida = self.verificaPontosdeVida()
        if forca < teste:
            print("Você falhou no teste")
            vida = int((vida / 3))
            personagem.subPontosDeVida(vida)
        else:
            print("Você Passou no teste")


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
    input("Força, Constituição, Tamanho, Destresa, Aparencia, Inteligência, Poder e Educação")
    resposta = input("Gostaria de saber mais sobre alguma dessas categorias ? (S/N): ")
    if resposta == "S":
        personagem.personagemNome()
        referencia = "0"
        while referencia == "0":
            print(
                "Qual categoria vc gostaria de saber ?  (1) Força, (2) Constituição, (3) Tamanho, (4) Destreza, (5) Aparencia, (6) Inteligência, (7) Poder  (8) Educação (9) Sair ")
            referencia = input()
            if referencia == "1":
                input("Força: Mede o poder muscular.")
                input(
                    "É usada para julgar o quanto se pode levantar, puxar ou empurrar, ou o quão firme pode-se segurar alguma coisa ...")
                input("Também é utilizada para calcular o dano em um combate corpo-a-corpo ... ")
                input("Se sua força for reduzida a 0, você se tornará um inválido incapaz de se levantar da cama ...")
                referencia = "0";

            elif referencia == "2":
                input("Constituição: Essa característica se compara a saúde, vigor e vitalidade.")
                input("Também é utilizado para verificar a resistencia a afogamentos ...")
                input("Venenos e doenças podem alterar diretamente a constituição do jogador ...")
                input(
                    "Jogadores com alta constituição sempre têm altos pontos de vida, resistindo a mais danos e ataques ...")
                input("Se sua constituição for reduzida a 0, você morre")
                referencia = "0";
            elif referencia == "3":
                input("Tamanho: Mede a altura e o peso em um unico número")
                input("Para enxergar por cima de alguma coisa, para se espremer sobre uma pequena abertura ...")
                input("ou até para julgar se a cabeça de alguem esta aparecendo sera levado em conta o tamanho ...")
                input("o tamanho também é levado em conta para determinar pontos de vida e dano extra ...")
                input("A perda de membros diminui-ra os pontos em tamanho, ou em destresa ...")
                input("Se seu tamanho for reduzido a 0, você desaparece ...")
                input("(Sabe-se la para onde)")
                input(".....")
                referencia = "0";
            elif referencia == "4":
                input("Destreza: Mede a ágilidade, e a flexibilidade física")
                input("É usado para calcular segurar um apoio antes de cair, ou para pegar algo sem ser notado ...")
                input(
                    "Um jogador sem destreza é descordenado, incapaz de realizar tarefas físicas sem um rolamento bem-sucedido em sorte ...")
                input("Em combate quanto maior ataca primeiro ou atira primeiro ...")
                input("Ou pode incapacitar um oponente antes que o inimigo possa atacar")
                referencia = "0";
            elif referencia == "5":
                input("Aparencia: Mostra a atratividade e afabilidade.")
                input("Essa habilidade é usada para tentar causar boa impressão inicial ou em encontros sociais ...")
                input("juntamente com um rolamento de Lábia ou Barganha ...")
                input("Aparencia mede o que se vê no espeljo, não a capacidade de liderança ou o carisma ...")
                input("Por isso pode não perdurar no encontro com outras pessoas ...")
                input("Se sua aparencia for igual a 0 você será terrivelmente feio ...")
                input("E provocara comentarios e choque em qualquer lugar")
                referencia = "0";
            elif referencia == "6":
                input("Inteligência: Representa o quanto o jogaodr é capaz de aprender, lembrar, analisar ...")
                input("e também estar consciente daquilo que o cerca.")
                input("Conceitos difíceis, planos ou palpites tem uma chance baixa de serem desenvolvidos ...")
                input("Por essa razão exigem uma inteligência alta, além disso ... ")
                input(
                    "Inteligência esta relacionado a raciocinio e não a educação formal, individuos com alta inteligência não necessariamente possuem estudos")
                referencia = "0";
            elif referencia == "7":
                input("Poder: Indica a força de vontade")
                input("Quanto maior o poder maior a aptidão a Magia ...")
                input("Poder não quantifica liderança, o que é uma questão de escolhas ...")
                input("tambem usa-se poder para testes de sorte ")
                input("um jogador com poder zero ou baixo será fraco contra ataques hipnoticos ou magicos ")
                referencia = "0";
            elif referencia == "8":
                input("Educação: É valor do conhecimento formal e factual possuído pelo jogador")
                input("Educação mede a informação não o uso inteligente dela ...")
                input("um jogador sem educação seria como um recém-nascido ou uma pessoa com amnésia ...")
                input("provavelmente curioso e crédulo ...")
                referencia = "0";
            elif referencia == "9":
                input("Saindo ....")
            else:
                print("Digite um numero valido")
                referencia = "0";

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
    else:
        variavel = 1

print("Bem Jogado !!")
