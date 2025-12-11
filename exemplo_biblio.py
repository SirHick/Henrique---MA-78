import random
import time
from datetime import datetime

print("Sistema Iniciado...")
time.sleep(2)

print("INICIADO!")
time.sleep(1)

num_Rifas = int(input("Digite até qual número foram vendidos na sua rifa: "))

print("3, 2, 1")
time.sleep(3)

print("FOI!")
time.sleep(0.5)

sorteio = random.randint(0, num_Rifas)
agora = datetime.now()

print("Número gerado: ", sorteio)
print("Horário", agora)