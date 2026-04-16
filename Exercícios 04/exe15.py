'''Implemente:
• Gere 100 dados
• Filtre apenas dados críticos
• Exiba somente os relevantes
'''

import random

for i in range(100):
    valor = random.randint(2, 350)
    if(valor > 250):
        print("Valor relevante: ", valor)