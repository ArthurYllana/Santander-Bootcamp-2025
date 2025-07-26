class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # Chamada ao construtor da classe pai
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

    def __str__(self):
        return self.cor

# Exemplos de uso
moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("Azul", "45678", 4)
carro.ligar_motor()

caminhao = Caminhao("Vermelho", "5647489", 9, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
