class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando a Bicileta !")
        print("Bicicleta parada !")

    def correr(self):
        print("Vrumm")

b1 = Bicicleta("Vermelho", "caloi", 2000, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(f"A cor da bicicleta é {b1.cor}, seu modelo é {b1.modelo}, ela é do ano de {b1.ano} e seu valor é de {b1.valor}" )

b2 = Bicicleta("verde", "monark", 2000, 1500)

b2.buzinar() # Bicicleta.buzinar(b2)
b2.correr()
b2.parar()

print(f"A cor da bicicleta é {b2.cor}, seu modelo é {b2.modelo}, ela é do ano de {b2.ano} e seu valor é de {b2.valor}" )

