'''Desenvolva:
• Cálculo de média
• Valor máximo
• Valor mínimo
'''

import random

lista = []

for i in range(20):
    valor = random.randint(1,40)
    lista.append(valor)
print("Valores: ", lista)

valorMax = max(lista)
valorMin = min(lista)

media = sum(lista) / len(lista)

print("=== DADOS RELEVANTES ===")
print("Valor Máximo: ", valorMax)
print("Valor Mínimo: ", valorMin)
print("Média dos Valores gerados: ", media)