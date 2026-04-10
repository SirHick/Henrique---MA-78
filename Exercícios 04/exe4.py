'''Crie um código que:
• Gere valores de pH
• Mostre os dados
• Alerta se estiver fora da faixa ideal (6 a 8)'''

import random

for i in range(20):
    valorpH = random.uniform(1, 14)
    print("Valor do pH: ", round(valorpH, 1))
    if(valorpH < 6 or valorpH > 8):
        print("ALERTA! Valor do pH fora do esperado")
        print("\n")
