'''Criar um script Python que:
1. Gere 20 leituras de nível (%)
2. Mostre os valores
3. Gere alerta se nível < 20% ou > 90%'''

import random

for i in range(20):
    nivelLiq = random.uniform(0,100)
    print("Nível do Líquido (%): ", round(nivelLiq))
    if(nivelLiq < 20 or nivelLiq > 90):
        print("ALARME! Algo errado com o nível\n")