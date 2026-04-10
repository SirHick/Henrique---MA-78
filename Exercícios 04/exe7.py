'''
Implemente:

• Geração de dados de vibração
• Identificação de valores acima do limite
• Emissão de alerta'''


import random

for i in range(20):
    vibracao = random.uniform(0.1, 5.5)
    print("Vibração (mm/s): ", round(vibracao,1))
    if(vibracao > 4.5):
        print("ALERTA! Nível crítico de vibração da máquina")
        print("\n")