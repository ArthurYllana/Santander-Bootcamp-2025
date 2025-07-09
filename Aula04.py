def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")


def depositar(valor):
    saldo = 500
    salor += valor


sacar(100)

#Estrutura condicionais 

Maior_idade = 18
Idade_especial = 20

idade = int(input("Qual sua idade: "))

if idade >= Maior_idade:
    print("Maior de idade, pode tirar CNH")
elif idade == Idade_especial:
    print("Você já tem CNH.... EU SEI QUEM VOCÊ É")
else:
    print("Menor de idade, não pode tirar CNH, volte quando tiver 18")



saldo = 1000
saque = input(int("Digite o valor que deseja sacar: "))
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realziar o saque!")