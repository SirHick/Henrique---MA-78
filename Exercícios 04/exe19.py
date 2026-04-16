'''Implemente:
• Cálculo de eficiência (%)
• Comparação com meta 
'''

import random

lista = []

for i in range(20):
    valor = random.randint(1, 130)
    lista.append(valor)

media = sum(lista) / len(lista)

meta = 70

if(media > meta):
    print("Parabéns! Atingiu ou passou a % (porcentagem) da meta.")
else:
    print("Reprovou! Não atingiu a % (porcentagem) da meta.")