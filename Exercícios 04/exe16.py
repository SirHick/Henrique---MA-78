'''
Crie um programa que:
• Gere dados
• Simule envio para nuvem
• Exiba mensagem de envio '''

import random

lista = []

for i in range(20):
    temp = random.uniform(30, 120)
    if(temp >= 100):
            lista.append(round(temp,2))
            print("Dados relevantes de temperatura obtidos: ", lista)
            print("Enviando para a nuvem...")

