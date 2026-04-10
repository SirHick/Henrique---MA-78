'''Crie um script que:
• Receba um valor de temperatura
• Se > 80 → desligar máquina
• Caso contrário → operação normal'''

import random

for i in range(20):
    temp = random.uniform(30, 90)
    print("Temperatura: ", round(temp,1))
    if(temp > 80):
        print("TEMPERATURA > 80°C | DESLIGANDO MÁQUINA...")
        print("\n")
    else:
        print("TEMPERATURA IDEAL | OPERAÇÃO NORMAL...")
        print("\n")