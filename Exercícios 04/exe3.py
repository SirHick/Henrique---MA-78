'''Implemente um script que:
• Gere 20 valores de consumo energético
• Exiba os dados
• Gere alerta se consumo ultrapassar o limite definido '''

import random

for i in range (20):
    conEnergia = random.uniform(100, 400)
    print("Consumo Energético (kWh): ", round(conEnergia,2))
    if(conEnergia > 300):
        print("ALERTA! Consumo acima do esperado.")
        print("\n")