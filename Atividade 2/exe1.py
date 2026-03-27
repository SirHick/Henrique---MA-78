import random 
 
for i in range(20):
    temperatura = random.uniform(20,40)
    pressao = random.uniform(1, 8)
    print("Temperatura: ", round(temperatura,2), "\n", "Pressão: ", round(pressao,2))
    print("\n")
    if(temperatura > 35):
        print("ALARME! Temperatura muito alta!\n")