'''
Controle de Esteira com Sensor de Presença
Uma esteira transportadora deve ligar apenas quando um sensor detectar a presença de caixas.

Simule um sensor binário (0/1).
Ligue/desligue a esteira automaticamente.
Conte quantas caixas passaram em um período.
'''

import time, random

caixas_passada = 0

paradaMaquina = 0

for i in range (20):
    leituras_do_sensor = random.randint(0,1)
    if(leituras_do_sensor == 1):
        print("Esteira ligada. 1")
        caixas_passada += 1
    else: 
        paradaMaquina += 1
        print("Esteira desligada. 0")

print("Total de caixas passada na esteira: ", caixas_passada)

print("Total de vezes que a esteira parou hoje: ", paradaMaquina)