#Manipulando Arquivos em Python

arquivo = open("Santander-Bootcamp-2025/Parte 3/teste.txt", "r")
#print(arquivo.read())
#for linha in arquivo.readline():
    #print(linha)
print(arquivo.readlines())

while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()