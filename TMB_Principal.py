def calcular_imc():#função para calcular o IMC do usuário.

    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    imc = peso / ((altura / 100) ** 2)#Aqui os dados inseridos pelo usuário são usados para calcular o IMC.

    if imc < 18.5:#O método if verifica em qual faixa de IMC o usuário se encontra e exibe a classificação correspondente.
            return print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
    elif imc < 25:
            return print(f"Seu IMC é {imc:.2f}. Você está com peso normal.")
    elif imc < 30:
            return print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
    elif imc < 35:
            return print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau I.")
    elif imc < 40:
            return print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau II.")
    else:
            return print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau III.")

def calcular_tmb():#função para calcular a TMB do usuário.    
    
    peso = float(input("Digite o seu peso em KG: "))
    altura = float(input("Digite sua altura em CM: "))
    idade = float(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ")
    
#Cálculo da TMB usando a fórmula de Mifflin-St Jeor, que varia dependendo do sexo do usuário.

    if sexo.upper() == "M":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo.upper() == "F":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:#Método para tratar entradas inválidas de sexo, caso o usuário digite algo diferente de M ou F.
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
        return 
    
    print('''Digite seu nivel de atividade fisica:
          1. Sedentário
          2. Levemente ativo (1 a 3 x por semana)
          3. Moderadamente ativo (3 a 5 x por semana)
          4. Muito ativo (6 a 7 x por semana)''')
    
    nivel = int(input("Opção: "))
    
    #Cálculo da TMB ajustada pelo nível de atividade física do usuário, multiplicando a TMB calculada pelo fator correspondente ao nível de atividade.
    fatores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}#Dicionário que associa cada nível de atividade física a um fator multiplicador para ajustar a TMB.
    if nivel in fatores:
        tmb *= fatores[nivel]
    else:
        print("Nível de atividade inválido. Por favor, digite um número entre 1 e 4.")
        return 

#O método print() exibe a TMB calculada para o usuário, formatando o valor com duas casas decimais.
    print(f"Sua Taxa Metabólica Basal é: {tmb:.2f} kcal / dia")

def menu():#função para permitir que o usuário escolha entre calcular IMC ou TMB.
#A função exibe um menu de opções e chama a função correspondente com base na escolha do usuário.

    while True:
     print("Escolha uma opção: ")
     print("1. Calcular IMC")
     print("2. Calcular TMB")
     print("3. Sair")
     
     try:#Bloco try-except para tratar entradas inválidas do usuário, garantindo que apenas números sejam aceitos como opções.
        opcao = int(input("Opção: "))
     except ValueError:
        print("Opção inválida. Por favor, digite um número inteiro.")
        continue
        
#Se a opção escolhida for 1, chama a função calcular_imc().
     if opcao == 1:
          calcular_imc()
     elif opcao == 2:# Se a opção escolhida for 2, chama a função calcular_tmb().
          calcular_tmb()
     elif opcao == 3:#Se a opção escolhida for 3, encerra o programa.
        print("Saindo do programa...")
        break
     else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def principal():#função principal do programa que apresenta a finalidade da aplicação e chama a função escolha().
    
    print("Olá! Esta é uma aplicação para calcular seu indice de massa corporal (IMC) e Taxa Metabólica Basal (TMB).")
#Função que chama a função escolha() para permitir que o usuário escolha entre calcular IMC ou TMB.
    menu()

if __name__ == "__main__":#Verifica se o script está sendo executado diretamente (não importado como módulo) e chama a função principal.
    principal()