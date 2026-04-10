'''Desenvolva um programa em Python que:
• Gere 20 valores aleatórios de temperatura
• Exiba os dados coletados
• Gere um alerta quando a temperatura ultrapassar 80°C'''

import random 
 
for i in range(20):
    temperatura = random.uniform(30,110)
    print("Temperatura: ", round(temperatura,2))
    print("\n")
    if(temperatura > 80):
        print("ALARME! Temperatura muito alta!\n")