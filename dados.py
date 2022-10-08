import random

class dados():

    def rolagemSimples():
        dado = random.randint(1,99)
        print("Você tirou o numero {}".format(dado))
        return dado
    def rolagemHabilidade():
        referencia = 0
        numeros = 0
        while referencia < 3:
            input("Pressione Enter para rolar o dado")
            Numero = random.randint(1,6)
            print("Você tirou o numero {}".format(Numero))
            numeros = (Numero + numeros)
            referencia += 1
        input("Seu Total de pontos foi {}".format(numeros))
        return numeros
    def testeDehabilidade(habilidade):
        dado = dados.rolagemSimples()
        pontos = habilidade * 5
        if dado > pontos:
            if (dado-pontos) > 40:
                print("Você teve uma falha critica")
                return (habilidade/3)
            else:
                print("Você falhou no teste de habilidade")
                return (habilidade/5)
        else:
            print("você passou no teste de Habilidade")
            return 0
    def probabilidade(habilidade):
        chance = 100 - (100 - (habilidade * 5 ))
        print(f'Você tem {chance}% de chance de passar no teste')







