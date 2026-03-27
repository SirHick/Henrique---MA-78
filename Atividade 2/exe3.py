'''Criar um script Python que:
1. Gere 20 leituras de consumo (kWh)
2. Exiba os valores
3. Gere alerta se consumo > 500 kWh'''

import random

for i in range(20):
    consumo = random.uniform(100, 650)
    print("Consumo (kWh): ", round(consumo,1))
    if(consumo > 500):
        print("ALARME! Consumo muito alto\n")