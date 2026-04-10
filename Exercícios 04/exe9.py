'''Desenvolva:
• Lista de produção por hora
• Cálculo da média
• Verificação se meta foi atingida'''

import random

for i in range(24):
    unidadesProd = random.randint(500,2500)
    print("Unidades Produzidas: ", unidadesProd)
    
soma = 0

soma += unidadesProd

media = soma / 24

if(media > 70):
    print("\nMédia da Produção: ", media)
    print("META ATINGIDA!")
else:
    print("Média da Produção: ", media)
    print("META NÃO ATINGIDA!")