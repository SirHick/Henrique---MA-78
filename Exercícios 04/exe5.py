'''Desenvolva um programa que:
• Gere leituras de temperatura
• Mostre os dados
• Alerta se ultrapassar 10°C'''

import random

for i in range(20):
    temp = random.uniform(-8, 12)
    print("Temperatura: ", round(temp,1))
    if(temp > 10):
        print("ALERTA! Temperatura acima de 10°C")
        print("\n")