# encoding: utf-8

from personagem import personagem
from resposta import resposta
from dados import dados
from arvoreDecisao import arvoreDecisao

variavel = 0

while variavel == 0:
    nome = ""
    input("Pressione enter para começar ")
    while nome == "":
        nome: str = input("Digite seu nome:  ")
        if nome == "":
            print("Nome inválido")
    personagem = personagem(nome)
    input("Olá {} vamos começar criando seu personagem".format(personagem.nome))
    input("Começaremos Distribuindo seus pontos de habilidade")
    input("Seus pontos de Habilidade são divididos em 9 categorias")
    input("Força, Constituição, Tamanho, Destresa, Aparencia, Inteligência, Poder e Educação")
    print("Gostaria de saber mais sobre alguma dessas categorias ? (S/N): ")
    if resposta("S", "N"):
        referencia = "0"
        while referencia == "0":
            print(
                "Qual categoria vc gostaria de saber ?  (1) Força, (2) Constituição, (3) Tamanho, (4) Destreza, (5) Aparencia, (6) Inteligência, (7) Poder  (8) Educação (9) Sanidade (10) Pontos de Vida (11) Sair ")
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
                input("Sanidade: Define o quanto você consegue lidar com coisas que não deveriam exirtir ")
                input("Uma sanidade alta significa uma mente forte capaz de resistir ...")
                input("O valor de sanidade maxima é calculada a partir do seu poder ...")
                input("Se você ver algo que não deveria, choques emocionais grandes ou coisas sem sentidos ...")
                input("Fazem com que você perca Pontos de Sanidade ...")
                input("Se sua Sanidade chegar a zero, você não mais é capaz de controlar os seus atos ...")
                referencia = "0";
            elif referencia == "10":
                input("Pontos de Vida: Todos os seres vivos possuem pontos de vida ")
                input("Os pontos de vida são uma medía entre seu tamanho e a sua constituição ...")
                input("Sempre que você se machuca, você perde pontos de vida ...")
                input("Você ganha pontos de vida com tratamentos medicos, curativos ...")
                input("E também muito lentamente com o passar dos dias ...")
                input("Se seus pontos de vida chegarem a zero, você morre e o jogo acaba ...")
                referencia = "0";
            elif referencia == "11":
                input("Saindo ....")
                referencia = "1";

            else:
                print("Digite um numero valido")
                referencia = "0";

    input("Os pontos são calculados por meio da rolagem de dados")
    input("O dado sempre tera uma indicação D seguido do numero de lados")
    input("Nesse caso usaramos um D6 em 3 rolagens")
    input("Existem duas maneiras de distribuir os pontos a 'Tradicional' e a 'Por escolha' ")
    print("Gostaria de Saber mais sobre os tipos de Rolagem ? (S/N) ")
    if resposta("S", "N"):
        input("A Forma tradicional de rolagem, você escolhe para qual habilidade gostaria de fazer a rolagem")
        input("Em seguida a rolagem dos dados e feita e os pontos são Adicionados na habilidade")
        input("A rolagem por escolha, primeiro rolamos os dados e depois você decide onde quer adiconar")
        input("Os pontos de Habilidade")
    input("Lembrando que os pontos de vida são calculador, pela media de tamanho e constituição")
    input("E os de Sanidade por seu total de poder")
    input("Por isso não se pode adicionar pontos diretamente a eles")
    print("Qual forma você gostaria de Usar Tradicional ou Escolha? (T/E)")
    if resposta("T", "E"):
        input("Vamos começar escolhando a habilidade")

        referencia = 10
        while referencia != 0:
            print("\n ")
            print(
                "Para qual habilidade você gostaria de rolar ? (1) Força, (2) Constituição, (3) Tamanho, (4) Destreza, (5) Aparencia, (6) Inteligência, (7) Poder  (8) Educação")
            referencia = ""
            referencia = input()
            if referencia == "1" and personagem.forca == 0:
                numero = dados.rolagemHabilidade()
                personagem.addForca(numero)
            elif referencia == "2" and personagem.const == 0:
                numero = dados.rolagemHabilidade()
                personagem.addConst(numero)
            elif referencia == "3" and personagem.tam == 0:
                numero = dados.rolagemHabilidade()
                personagem.addTam(numero)
            elif referencia == "4" and personagem.des == 0:
                numero = dados.rolagemHabilidade()
                personagem.addDes(numero)
            elif referencia == "5" and personagem.apa == 0:
                numero = dados.rolagemHabilidade()
                personagem.addApa(numero)
            elif referencia == "6" and personagem.int == 0:
                numero = dados.rolagemHabilidade()
                personagem.addInt(numero)
            elif referencia == "7" and personagem.pod == 0:
                numero = dados.rolagemHabilidade()
                personagem.addPod(numero)
            elif referencia == "8" and personagem.edu == 0:
                numero = dados.rolagemHabilidade()
                personagem.addEdu(numero)
            else:
                if personagem.forca != 0 and referencia == "1":
                    print("Você já rolou para força")
                elif personagem.const != 0 and referencia == "2":
                    print("Você já rolou para constituição")
                elif personagem.tam != 0 and referencia == "3":
                    print("Você já rolou para tamanho")
                elif personagem.des != 0 and referencia == "4":
                    print("Você já rolou para destreza")
                elif personagem.apa != 0 and referencia == "5":
                    print("Você já rolou para aparência")
                elif personagem.int != 0 and referencia == "6":
                    print("Você já rolou para inteligência")
                elif personagem.pod != 0 and referencia == "7":
                    print("Você já rolou para poder")
                elif personagem.edu != 0 and referencia == "8":
                    print("Você já rolou para educação")

                else:
                    print("Digite uma resposta Valida")
            if personagem.forca != 0 and personagem.const != 0 and personagem.tam != 0 and personagem.des != 0 and personagem.apa != 0 and personagem.int != 0 and personagem.pod != 0 and personagem.edu != 0:
                referencia = 0



    else:
        contador = 8
        input("Vamos começar rolando os dados")
        while contador != 0:
            contador1 = 0
            numero = dados.rolagemHabilidade()
            print(
                "Para qual habilidade você quer add os pontos ? (1) Força, (2) Constituição, (3) Tamanho, (4) Destreza, (5) Aparencia, (6) Inteligência, (7) Poder  (8) Educação ")
            referencia = input()
            while contador1 == 0:
                if referencia == "1" and personagem.forca == 0:
                    personagem.addForca(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "2" and personagem.const == 0:
                    personagem.addConst(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "3" and personagem.tam == 0:
                    personagem.addTam(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "4" and personagem.des == 0:
                    personagem.addDes(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "5" and personagem.apa == 0:
                    personagem.addApa(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "6" and personagem.int == 0:
                    personagem.addInt(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "7" and personagem.pod == 0:
                    personagem.addPod(numero)
                    contador -= 1;
                    contador1 = 1;

                elif referencia == "8" and personagem.edu == 0:
                    personagem.addEdu(numero)
                    contador -= 1;
                    contador1 = 1;

                else:
                    if personagem.forca != 0 and referencia == "1":
                        print("Você já Adicionou pontos em força")
                    elif personagem.const != 0 and referencia == "2":
                        print("Você já Adicionou pontos em constituição")
                    elif personagem.tam != 0 and referencia == "3":
                        print("Você já Adicionou pontos em tamanho")
                    elif personagem.des != 0 and referencia == "4":
                        print("Você já Adicionou pontos em destreza")
                    elif personagem.apa != 0 and referencia == "5":
                        print("Você já Adicionou pontos em aparência")
                    elif personagem.int != 0 and referencia == "6":
                        print("Você já Adicionou pontos em inteligência")
                    elif personagem.pod != 0 and referencia == "7":
                        print("Você já Adicionou pontos em poder")
                    elif personagem.edu != 0 and referencia == "8":
                        print("Você já Adicionou pontos em educação")
                    else:
                        print("Digite uma resposta valida")
                        referencia = input()

    print("Você concluiu a distribuição de pontos")
    print("\n ")
    personagem.CalculaPontosDeVida()
    personagem.CalculaSanidade()
    input("Saindo ....")
    input("Um resumo rapido sobre rolagem de dados")
    input("A rolagem de dados é feita multiplicando a habilidade por 5")
    input("É rolando o dado, o valor do dado precisa ser menor que a habilidade")
    input("Exemplo: se o jogador possui 10 em força, será feito 10*5 = 50")
    input("Digamos que o jogar role 40 no dado, ele tera passado no teste")
    input("Se o resto for maior que 40, será considerado uma falha critica")
    input("Isso pode ser calculado diminuindo o poder de habilidade ao rolamento ")
    input("Exemplo 8 de habilidade, 8*5 = 40, com um dado com rolamento 80, temos 80-40 = 40 = falha critica")
    input("Uma falha critica faz com que o jogador tenha mais consequencias pela sua falha na habilidade")
    input("Presione enter para começar a história")
    while personagem.pontosDeVida != 0:
        input("A noite parece começar calma, embora as semanas chuvosas que deixam o clima úmido e pegajoso")
        input(
            "{} vai para a aula com a cabeça abaixada tentando se desviar da fraca chuva que cai sobre a cidade".format(
                personagem.nome))
        input("sua jaqueta já se encontra parcialmente encharcada e seus tênis além de água também possuem barro. ")
        input("{}:  -Isso que estou apenas indo, imagina depois dessa aula chata".format(personagem.nome))
        dados.testeDehabilidade(personagem.forca)
        input(f'{personagem.nome} continua caminhando ')
        input(f'-ohh {personagem.nome}, como você esta ? indo para aula ?')
        resposta = input('1 - Oi, estou bem e você 2-Ãn ? 3- Indo, como uma vaca vai para o abate')
        arvoreDecisao(resposta, "1 2 3")
        if resposta == "1":
            input('Desconhecido - Estou bem também um pouco descontente com o clima haha')
        elif resposta == "2":
            input('Desconhecido - Você não deve estar conseguindo me ver pela chuva')
        else:
            input("Desconhecido - Dramatico e preciso como sempre")
        input('Francisco - Não sei se lembra de mim, sou seu colega Francisco')
        input('Francisco - Sempre bom ver uma cara conhecida')
        input('Francisco parece bem animado em ver você, apesar da chuva e frio')
        input(
            'Francisco - Pensei que iria acabar sendo somente eu na aula de hoje, visto a chuva e ser uma quarta-feira')
        input('Francisco - Essa cadeira esta muito complexa, não quis faltar a aula e arriscar entender menos ainda')
        input('Francisco sorri como se estivesse falando de algo deveras interessante')
        input('Talvez você devesse ter o animo de Francisco')
        input('Vocês continuam a caminhada pelo campus, passando pelo grande portal da entrada')
        input('Ele é um arco ornado com pedras com os dizeres:')
        input('"O sábio pode descobrir o mundo sem transpor a sua porta. Vê sem olhar, realiza sem agir."')
        input('Sempre penso no que essa frase quer dizer, nunca encontro uma resposta curta')
        input('Passamos pelas outras partes do campus ate chegar ao centro de convivencias')
        input('Chegando lá encontramos alguns colegas da computação e fomos para a aula')
        input('Saindo da aula, com mais sonos do que entrei, eu parecia um zumbi indo para casa')
        input('Estava quase no portal, quando enxerguei uma pequena luz em um dos predios antigos')
        resp = 3
        cont = 3
        while cont == 3:
            resp = input('1 - investigar 2 - seguir caminho:  ')
            resp = (arvoreDecisao(resp, "1 2"))
            if resp == "2":
                print("Você não consegue simplesmente seguir seu caminho")
            else:
                cont = 1
        input("Você se aproxima ... ")
        input("A fagulha brilha na escuridão")
        input("É um brilho vermelho como o fogo, você pensa em como com a chuva aquilo parece acesso")
        input("Você encherga um simbolo no chão")
        input("O que você deseja fazer ? 1 - investigar simbolo 2 - focar na fagulha 3 - observar em volta")
        resp = (arvoreDecisao(resp,"1 2 3"))
        if resp == "1":
            input("Você esta tentando verificar o simbolo no chão, você necessita de conhecimento para saber qual é o simbolo")
            dados.probabilidade(personagem.edu)
            input("Pressione enter para rolar")
            x = dados.testeDehabilidade(personagem.edu)
            personagem.subPontosSanidade(x)
            if personagem.doido(): break
            if x > 0:
                input('O simbolo no chão é algo que se assemelha a um pentagrama, mas esse é difeerenete ')
                input('Esse representa um simbolo de proteção, estava protegendo a fagulha ou algo em volta dela')
            else:
                input('Algo perturbou a sua mente, aquele simbolo não deveria estar ali')
                input('Aquela fagulha não deveria estar ali')
        elif resp == "2":
            input("Você foca na fagulha, tenta entender o que esta acontecendo")
            input('Algo parece estranho, algo não faz sentido')
            input("Sua sanidade esta sendo testada, pressione enter para rolar o dado")
            dados.probabilidade(personagem.san)
            personagem.subPontosSanidade(dados.testeDehabilidade(personagem.san))
        else:
            input('Você tenta olhar em volta, mas não consegue')
            input("Seu foco passa a ser somente a fagulha")
            input('Em uma nova tentativa de Olhar você encontra algo')
            input('A algo ou alguem por detrásda fagulha')







    texto = input("Recomeçar? S/N: ")
    if texto == "S":
        variavel = 0
    else:
        variavel = 1

print("Bem Jogado !!")
