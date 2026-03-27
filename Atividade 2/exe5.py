'''Criar um script Python que:
1. Gere 20 leituras de temperatura (°C)
2. Exiba os valores
3. Gere alerta se temperatura > 10°C '''

import random

for i in range(20):
    temperatura = random.uniform(-20,12)
    print("Temperatura (°C): ", round(temperatura))
    if(temperatura > 10):
        print("ALARME! Temperatura fora do aceitável\n")