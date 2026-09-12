
def escolha():

    print("Para começar, escolha uma opção: ")
    print("1. Calcular IMC")
    print("2. Calcular TMB")

    n = int(input("Opção: "))

    if n == 1:
        imc()
    elif n == 2:
        tmb()

def principal():

    print("Olá! Esta é uma aplicação para calcular seu IMC e Taxa Metabólica Basal (TMB).")

    escolha()

principal()





  