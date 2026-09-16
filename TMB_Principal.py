#Importação das bibliotecas necessárias para a criação da interface gráfica e exibição de mensagens de erro ou informações.
import tkinter as tk
import tkinter.messagebox as messagebox

#           ||||PROCESSAMENTO DOS DADOS||||
def calcular_imc(peso_str, altura_str):#função para calcular o IMC do usuário.

    try:
        peso = float(peso_str)
        altura = float(altura_str)
        imc = peso / ((altura / 100) ** 2)#Aqui os dados inseridos pelo usuário são usados para calcular o IMC.
#Try e except são usados para tratar possíveis erros de conversão de string para float, caso o usuário insira valores não numéricos.
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")
        return

    if imc < 18.5:#O método if verifica em qual faixa de IMC o usuário se encontra e exibe a classificação correspondente.
            classificacao = "Você está abaixo do peso."
    elif imc < 25:
            classificacao = "Você está com peso normal."
    elif imc < 30:
            classificacao = "Você está com sobrepeso."
    elif imc < 35:
            classificacao = "Você está com obesidade grau I."
    elif imc < 40:
            classificacao = "Você está com obesidade grau II."
    else:
            classificacao = "Você está com obesidade grau III."

#            ||||POP-UP DE RESULTADO||||

    messagebox.showinfo("Resultado do IMC", f"Seu IMC é: {imc:.2f}\n{classificacao}")

def calcular_tmb(peso_str, altura_str, idade_str, sexo_str, nivel_str):#função para calcular a TMB do usuário.
    
    peso = float(peso_str)
    altura = float(altura_str)
    idade = float(idade_str)
    sexo = sexo_str
    nivel = int(nivel_str)
    
#Cálculo da TMB usando a fórmula de Mifflin-St Jeor, que varia dependendo do sexo do usuário.

    if sexo.upper() == "M":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo.upper() == "F":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:#Método para tratar entradas inválidas de sexo, caso o usuário digite algo diferente de M ou F.
        messagebox.showerror("Erro", "Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
        return 
    
    #Cálculo da TMB ajustada pelo nível de atividade física do usuário, multiplicando a TMB calculada pelo fator correspondente ao nível de atividade.
    fatores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}#Dicionário que associa cada nível de atividade física a um fator multiplicador para ajustar a TMB.
    if nivel in fatores:
        tmb *= fatores[nivel]
    else:
        messagebox.showerror("Erro", "Nível de atividade inválido. Por favor, digite um número entre 1 e 4.")
        return 

#O método print() exibe a TMB calculada para o usuário, formatando o valor com duas casas decimais.
    messagebox.showinfo("Resultado da TMB", f"Sua Taxa Metabólica Basal é: {tmb:.2f} kcal / dia")

#            ||||Gerenciamento de telas||||

def limpar_tela():
    
    for widget in janela.winfo_children():#O método winfo_children() retorna uma lista de todos os widgets filhos da janela principal (root).
        widget.destroy()#O método destroy() é chamado em cada widget para removê-lo da tela, limpando assim a interface gráfica.
        
def tela_menu():#função para permitir que o usuário escolha entre calcular IMC ou TMB.
#A função exibe um menu de opções e chama a função correspondente com base na escolha do usuário.
    limpar_tela()
    #Titulo do menu principal, exibido na interface gráfica.
    lbl_titulo = tk.Label(janela, text="Calculadora de Saúde", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white")
    lbl_titulo.pack(pady=20)

    # Botão IMC
    btn_imc = tk.Button(janela, text="Calcular IMC", font=("Segoe UI", 11), width=20, bg="#3498db", fg="white", relief="flat", command=tela_imc)
    btn_imc.pack(pady=10, ipady=5)

    # Botão TMB
    btn_tmb = tk.Button(janela, text="Calcular TMB", font=("Segoe UI", 11), width=20, bg="#2ecc71", fg="white", relief="flat", command=tela_tmb)
    btn_tmb.pack(pady=10, ipady=5)

    # Botão Sair
    btn_sair = tk.Button(janela, text="Sair", font=("Segoe UI", 11), width=20, bg="#e74c3c", fg="white", relief="flat", command=janela.quit)
    btn_sair.pack(pady=10, ipady=5)

def tela_imc():#função para exibir a tela de cálculo do IMC.
    
    limpar_tela()
    lbl_titulo = tk.Label(janela, text="Calculadora de IMC", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white")
    lbl_titulo.pack(pady=20)

    # Entrada de Peso
    lbl_peso = tk.Label(janela, text="Peso (kg):", font=("Segoe UI", 11), bg="#2c3e50", fg="white")
    lbl_peso.pack(pady=5)
    entry_peso = tk.Entry(janela, font=("Segoe UI", 11))
    entry_peso.pack(pady=5)

    # Entrada de Altura
    lbl_altura = tk.Label(janela, text="Altura (cm):", font=("Segoe UI", 11), bg="#2c3e50", fg="white")
    lbl_altura.pack(pady=5)
    entry_altura = tk.Entry(janela, font=("Segoe UI", 11))
    entry_altura.pack(pady=5)

    # Botão Calcular IMC
    btn_calcular = tk.Button(janela, text="Calcular IMC", font=("Segoe UI", 11), width=20, bg="#3498db", fg="white", relief="flat",
                             command=lambda: calcular_imc(entry_peso.get(), entry_altura.get()))
    btn_calcular.pack(pady=10, ipady=5)

    # Botão Voltar
    btn_voltar = tk.Button(janela, text="Voltar ao Menu", font=("Segoe UI", 11), width=20, bg="#95a5a6", fg="white", relief="flat",
                           command=tela_menu)
    btn_voltar.pack(pady=10, ipady=5)
    
def tela_tmb():#função para exibir a tela de cálculo da TMB.
    
    limpar_tela()
    
    lbl_titulo = tk.Label(janela, text="Calculadora de TMB", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white")
    lbl_titulo.pack(pady=20)

    lbl_titulo = tk.Label(janela, text="Cálculo de TMB", font=("Segoe UI", 14, "bold"), bg="#2c3e50", fg="white")
    lbl_titulo.pack(pady=10)

    # Campos de Entrada
    tk.Label(janela, text="Peso (kg):", bg="#2c3e50", fg="white").pack()
    ent_peso = tk.Entry(janela)
    ent_peso.pack(pady=2)

    tk.Label(janela, text="Altura (cm):", bg="#2c3e50", fg="white").pack()
    ent_altura = tk.Entry(janela)
    ent_altura.pack(pady=2)

    tk.Label(janela, text="Idade:", bg="#2c3e50", fg="white").pack()
    ent_idade = tk.Entry(janela)
    ent_idade.pack(pady=2)

    # Seleção do Sexo (Radiobutton)
    var_sexo = tk.StringVar(value="M")
    frame_sexo = tk.Frame(janela, bg="#2c3e50")
    frame_sexo.pack(pady=5)
    
    tk.Radiobutton(frame_sexo, text="Masculino", variable=var_sexo, value="M", bg="#2c3e50", fg="white", selectcolor="#34495e").pack(side="left")
    tk.Radiobutton(frame_sexo, text="Feminino", variable=var_sexo, value="F", bg="#2c3e50", fg="white", selectcolor="#34495e").pack(side="left")

    # Seleção do Nível de Atividade (OptionMenu)
    tk.Label(janela, text="Nível de Atividade Física:", bg="#2c3e50", fg="white").pack(pady=(5, 0))
    
    opcoes_atividade = {
        "1. Sedentário": 1,
        "2. Levemente ativo (1-3x/sem)": 2,
        "3. Moderadamente ativo (3-5x/sem)": 3,
        "4. Muito ativo (6-7x/sem)": 4
    }
    
    var_atividade = tk.StringVar(value="1. Sedentário")
    menu_atividade = tk.OptionMenu(janela, var_atividade, *opcoes_atividade.keys())
    menu_atividade.pack(pady=5)

    # Botão Calcular
    btn_calc = tk.Button(
        janela, text="Calcular", bg="#2ecc71", fg="white", font=("Segoe UI", 10, "bold"), relief="flat",
        command=lambda: calcular_tmb(
            ent_peso.get(), 
            ent_altura.get(), 
            ent_idade.get(), 
            var_sexo.get(), 
            opcoes_atividade[var_atividade.get()]
        )
    )
    btn_calc.pack(pady=10, ipadx=10, ipady=3)

    # Botão Voltar
    btn_voltar = tk.Button(janela, text="Voltar ao Menu", bg="#7f8c8d", fg="white", relief="flat", command=tela_menu)
    btn_voltar.pack(pady=5)
    
#            ||||Inicialização da Janela Principal||||
janela = tk.Tk()
janela.title("Calculadora de Saúde")
janela.configure(bg="#2c3e50")

# Centralização da Janela na Tela
largura = 350
altura = 450
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

tela_menu()

janela.mainloop()