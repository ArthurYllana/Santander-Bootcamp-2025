#Estutura de repetição 
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end ="")

print()

#range(stop) -> range object
#range(start, stop[, step]) -> range object

#tabuada do 5
for numero in range (0, 51, 5):
    print(numero, end=" ")

#while 
print()
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Volte sempre")
    