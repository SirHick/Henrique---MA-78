'''Implemente:
• Lista de valores
• Identificação de alarmes
• Contagem de falhas'''

import random

contFalha = 0

for i in range(20):

    valor = random.randint(1,10)
    print("Valor lido: ", valor)
    print("\n")

    if(valor > 8):
        print("ALERTA! Valor maior que 6.7")
        contFalha += 1
        print("\n")

print("TOTAL DE FALHAS: ", contFalha)