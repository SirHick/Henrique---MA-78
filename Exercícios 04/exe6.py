'''Crie um script que:
• Gere níveis de tanque (%)
• Exiba os dados
• Alerta se nível estiver crítico (<20% ou >90%)'''

import random 

for i in range(20):
    nivelTanque = random.uniform(10,95)
    print("Nível do Tanque (%): ", round(nivelTanque))
    if(nivelTanque < 20 or nivelTanque > 90):
        print("ALERTA! Nível do tanque está crítico.")
        print("\n")