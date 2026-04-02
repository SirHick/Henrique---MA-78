#Criar um script Python que:
#1. Gere 20 leituras de velocidade (m/s)
#2. Mostre os valores na tela
#3. Gere alerta se velocidade < 0.5 m/s 

import random

for i in range(20):
    velocidade = random.uniform(0.1, 1.0)
    print("Velocidade (m/s): ", round(velocidade,1))
    if(velocidade < 0.5):
        print("\nALARME! Velocidade muito baixa!\n")
