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
            input("Pressione qualquer tecla para rolar o dado")
            Numero = random.randint(1,6)
            print("Você tirou o numero {}".format(Numero))
            numeros = (Numero + numeros)
            referencia += 1
        input("Seu Total de pontos foi {}".format(numeros))
        return numeros



