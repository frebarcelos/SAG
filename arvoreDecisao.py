def arvoreDecisao(resposta,alternativas):
    verificador = 0
    lista = alternativas.split()
    while verificador == 0:
        for i in lista:
            if i == resposta:
                verificador = 1
                return resposta
        else:
            print('Digite uma resposta valida')
            resposta = input()



