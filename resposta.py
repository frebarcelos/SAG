
def resposta(sim,nao):
    resp = ""
    while resp != sim:
        resp = input()
        if resp == sim:
            resp = "N"
            return True
        elif resp == nao:
            resp = "N"
            return False

        else:
            print("Digite uma resposta Valida")
