from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV")
        print("Desligada")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar")
        print("Ligada")

    def desligar(self):
        print("Desligando o Ar")
        print("Desligada")

    @property
    def marca(self):
        return "Asus"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(f"Marca: {controle.marca}")

print("===================================")

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(f"Marca: {controle2.marca}")
