'''Criar um script Python que:
1. Gere 20 leituras de pH
2. Mostre os valores
3. Gere alerta se pH < 6 ou pH > 8'''

import random

for i in range(20):
    pH = random.uniform(1,14)
    print("pH: ", round(pH))
    if(pH < 6 or pH > 8):
        print("ALARME! pH não básico\n")