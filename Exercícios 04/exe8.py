'''Crie um programa que:
• Gere valores de pressão
• Exiba os dados
• Alerta se estiver fora do intervalo seguro'''

import random

for i in range(20):
    pressao = random.uniform(1, 10)
    print("Pressão (kPa): ", round(pressao,1))
    if(pressao > 8):
        print("ALERTA! Anomalia na pressão")
        print("\n")