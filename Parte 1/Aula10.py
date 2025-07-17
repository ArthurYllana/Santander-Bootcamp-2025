#Funções 

def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2(nome="Guilherme")
exibir_mensagem3()
exibir_mensagem3(nome="Chappie")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1998, "ABC-90887")

#def exibir_poema(data_extenso, *args, **kwargs):
   # texto = "\n".join([f"[{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    #mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    #print(mensagem)

#exibir_poema("Zen of Python", "Beautiful is better tahn ugly.", autor= "Tim Peters", ano=1999)

salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))