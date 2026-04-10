'''Crie um programa que:
• Gere 20 leituras de velocidade
• Mostre os valores
• Alerta se a velocidade for menor que 0.5 m/s'''

import random 

for i in range (20):
    velocidade = random.uniform(0.1, 5)
    print("Velocidade: ", round(velocidade,2))
    print("\n")
    if(velocidade < 0.5):
        print("ALERTA! Velocidade muito baixa.")