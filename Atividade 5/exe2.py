'''Controle de Temperatura de Forno Industrial
Um forno deve manter a temperatura entre 180°C e 200°C.

Simule a leitura de temperatura ao longo do tempo.
Acione um aquecedor quando estiver abaixo do limite.
Desligue ao atingir o limite superior.'''

import random 

for i in range(10):
    tempForno = random.randint(140, 201)
    if(tempForno < 180):
        print("\n", tempForno, "°C")
        print("\nAcionando aquecedor...")
    elif(tempForno > 200):
        print("\nDesligando forno")
        break
    else:
        print("\nOperando normalmente: ", tempForno, "°C")