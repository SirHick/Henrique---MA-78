'''
arquivo = open("teste.txt", "w")
arquivo.write(str(input("Digite um texto: ")))
arquivo.close()

arquivo = open("teste.txt", "r")
dados_Arq = arquivo.read()
print(dados_Arq)
arquivo.close()
'''
'''
with open("teste.txt", "w") as arquivo:
    arquivo.write("Python e demais.")

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

'''
'''
with open("teste.txt", "w") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Carlos\n")
    arquivo.write("Maria")

'''

'''
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
'''

import csv
with open("alunos.csv", "w", newline = "") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"]) #WRITEROW: escreve apenas em uma linha (exclusivo o csv)
    escritor.writerow(["Ana", 8])
    escritor.writerow(["Carlos", 7])
    escritor.writerow(["Rafael", 9])

with open("alunos.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)

import os

if os.path.exists("teste.txt"):
    print("Arquivo existente")
else:
    print("Arquivo inxistente")