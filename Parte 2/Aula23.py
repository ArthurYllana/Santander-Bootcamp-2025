#decoradores

def Calcular(operacao):
    def somar(a,b):
        return a + b
    def subtrair(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def dividir(a,b):
        return a/b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return mul
        case "/":
            return dividir
    
resultado = Calcular("+")(1,3)
print(resultado)



def mensagem(none):
    print("Executando mensagem")
    return f"Oi {none}"

def mensagem_longa(none):
    print("Executando mensagem longa")
    return f"Olá, tudo bem com vocÊ {none}?"

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, "Arthur"))
print(executar(mensagem_longa, "Arthur"))

#Função interna

def principal():
    print("Executando função principal")

    def funcao_interna():
        print("Executando a funcao interna")

    def funcao_2():
        print("Executando a função 2")

    funcao_interna()
    funcao_2()

principal()


def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")

    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()