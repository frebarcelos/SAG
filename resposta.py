
def resposta():
    resp = ""
    while resp != "N":
        resp = input()
        if resp == "S":
            resp = "N"
            return True
        elif resp == "N":
            resp = "N"
            return False

        else:
            print("Digite uma resposta Valida")
