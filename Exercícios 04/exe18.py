'''Crie um script que:
• Analise sequência de dados
• Detecte anomalias
• Gere alerta'''

import random
anomalia = 0
for i in range(20):
    num = random.randint(1,65)
    if(num > 50):
        anomalia += 1
        print("Anomalia detectada! Passou de 50")

print("Total Anomalias: ", anomalia)