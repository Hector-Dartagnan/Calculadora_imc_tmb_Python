def calcular_imc():

    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    imc = peso / ((altura / 100) ** 2)

    return imc

def calcular_tmb():
    peso = float(input("Digite o seu peso em KG: "))
    altura = int(input("Digite sua altura em CM: "))
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ")

    if sexo.upper() == "M":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo.upper() == "F":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
        return

    print(f"Sua Taxa Metabólica Basal é: {tmb:.2f} kcal / dia")

def tabela(imc):

    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está com peso normal.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    elif imc < 35:
        print("Você está com obesidade grau I.")
    elif imc < 40:
        print("Você está com obesidade grau II.")

def escolha():

    print("Para começar, escolha uma opção: ")
    print("1. Calcular IMC")
    print("2. Calcular TMB")

    opcao = int(input("Opção: "))

    if opcao == 1:
        imc = calcular_imc()
        tabela(imc)
    elif opcao == 2:
        calcular_tmb()

def principal():

    print("Olá! Esta é uma aplicação para calcular seu IMC e Taxa Metabólica Basal (TMB).")

    escolha()

if __name__ == "__main__":
    principal()



  