# Lista para armazenar as quantidades
listaQtd = []

# Função para receber as quantidades produzidas
def qtdProd():
    for i in range(0,5):  # Lista com apenas 5 valores
        while True:  # Validação de dados com while e try
            try:
                qtd = int(input("Digite a quantidade que foi produzida: "))
                listaQtd.append(qtd)
                break  # Segue adiante no código
            except:
                print("Valor inválido")
    print("Lista digitada:", listaQtd)

# Função para somar todos os valores
def totalProd():
    return sum(listaQtd)

# Função para calcular a média
def mediaProd():
    return sum(listaQtd) / 5

# Função para encontrar o maior valor
def maiorValor():
    return max(listaQtd)

# Função para encontrar o menor valor
def menorValor():
    return min(listaQtd)

# Função para mostrar o relatório
def relatorio():
    print("\n---RELATÓRIO DE PRODUÇÃO---\n")
    print("Total produzido: ", totalProd())
    print("Média produzida: ", mediaProd())
    print("Maior valor produzido: ", maiorValor())
    print("Menor valor produzido: ", menorValor())

# Menu
def menu():
    while True:
        continuar = input("\nVocê quer continuar? (S/N): ") #Variável para escolha final do usuário

        if continuar == "S": #Sistema de condição para usuário encerrar, ou não, o programa
            relatorio()
            listaQtd.clear() #Limpa a lista para o usuário adicionar os novos 5 valores 
            print("\n") #Apenas para pular uma linha
            qtdProd()
        elif continuar == "N":
            print("Tudo bem. Programa encerrado.")
            break

        else:
            print("Digite apenas S ou N.")
qtdProd()
menu()