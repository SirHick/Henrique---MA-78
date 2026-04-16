'''Crie um código que:
• Armazene dados em lista
• Mostre histórico
• Calcule média'''

lista = []

import random

for i in range(20):
    dados = random.randint(10, 30)
    lista.append(dados)
print("Dados gerados")

print("=== HISTÓRICO DE DADOS ===")
print(lista)
print("==========================")

media = sum(lista) / len(lista)
print("Média: ", media)