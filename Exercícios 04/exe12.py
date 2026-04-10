'''Crie um programa que:
• Classifique dados em:
o normal
o alerta
o crítico'''

import random

for i in range(20):
    dados = random.uniform(20,80)
    print("Dados: ", round(dados,1))

    if(dados >= 20 and dados <= 35):
        print("Operando normalmente\n")
    
    elif(dados >= 36 and dados <= 67):
        print("ALERTA\n")
    
    else:
        print("CRÍTICO\n")