'''Desenvolva um sistema que:
• Gere dados (sensor)
• Aplique lógica (CLP)
• Exiba dados (supervisório)
• Armazene (banco)
• Mostre relatório final (dashboard)
'''
import random

banco_de_dados = []
total_alertas = 0

print("\n--- EXIBINDO DADOS ---\n")

for i in range(10):
    
    temperatura = random.randint(10, 50)
    
    banco_de_dados.append(temperatura)
    
    if temperatura > 40:
        print("Temperatura:", temperatura, "°C - ALERTA: Muito quente!\n")
        total_alertas = total_alertas + 1
    elif temperatura < 20:
        print("Temperatura:", temperatura, "°C - ALERTA: Muito frio!\n")
        total_alertas = total_alertas + 1
    else:
        print("Temperatura:", temperatura, "°C - NORMAL\n")

media = sum(banco_de_dados) / len(banco_de_dados)
temp_maxima = max(banco_de_dados)

print("\n--- RELATÓRIO FINAL ---")
print("\nDados armazenados:", banco_de_dados, "\n")
print("Média de temperatura:", media, "\n")
print("Temperatura mais alta:", temp_maxima, "\n")
print("Total de alertas:", total_alertas, "\n")