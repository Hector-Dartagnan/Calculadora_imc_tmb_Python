def calcular_imc():#função para calcular o IMC (Índice de Massa Corporal) do usuário.
#Aqui solicitamos ao usuário que insira seu peso e altura.
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    imc = peso / ((altura / 100) ** 2)#Aqui os dados inseridos pelo usuário são usados para calcular o IMC.

    return imc#Método retorna o valor do IMC calculado para a função que chamou calcular_imc().

def calcular_tmb():
    #função para calcular a TMB (Taxa Metabólica Basal) do usuário.
    peso = float(input("Digite o seu peso em KG: "))
    altura = float(input("Digite sua altura em CM: "))
    idade = float(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ")
#Cálculo da TMB usando a fórmula de Harris-Benedict, que varia dependendo do sexo do usuário.
    if sexo.upper() == "M":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo.upper() == "F":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:#Método para tratar entradas inválidas de sexo, caso o usuário digite algo diferente de M ou F.
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
        return
#O método print() exibe a TMB calculada para o usuário, formatando o valor com duas casas decimais.
    print(f"Sua Taxa Metabólica Basal é: {tmb:.2f} kcal / dia")

def tabela(imc):
    #função para exibir a classificação do IMC com base no valor calculado seguindo as diretrizes da OMS.
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:#O método if verifica em qual faixa de IMC o usuário se encontra e exibe a classificação correspondente.
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está com peso normal.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    elif imc < 35:
        print("Você está com obesidade grau I.")
    elif imc < 40:
        print("Você está com obesidade grau II.")

def escolha():#função para permitir que o usuário escolha entre calcular IMC ou TMB.
#A função exibe um menu de opções e chama a função correspondente com base na escolha do usuário.
    print("Para começar, escolha uma opção: ")
    print("1. Calcular IMC")
    print("2. Calcular TMB")
#Guarda o valor da opção escolhida pelousuário em uma variável e converte para inteiro.
    opcao = int(input("Opção: "))
#Se a opção escolhida for 1, chama a função calcular_imc() e exibe a tabela de classificação do IMC.
    if opcao == 1:
        imc = calcular_imc()#Guarda o valor do IMC calculado em uma variável.
        tabela(imc)#Envia o valor do IMC para a função tabela() para exibir a classificação do IMC.
    elif opcao == 2:# Se a opção escolhida for 2, chama a função calcular_tmb().
        calcular_tmb()

def principal():#função principal do programa que apresenta a finalidade da aplicação e chama a função escolha().
    print("Olá! Esta é uma aplicação para calcular seu IMC e Taxa Metabólica Basal (TMB).")
#Função que chama a função escolha() para permitir que o usuário escolha entre calcular IMC ou TMB.
    escolha()

if __name__ == "__main__":#Verifica se o script está sendo executado diretamente (não importado como módulo) e chama a função principal.
    principal()



  