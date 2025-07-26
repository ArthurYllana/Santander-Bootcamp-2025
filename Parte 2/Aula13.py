#Método destruitvo

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("auaua")

    def __del__ (self):
        print("Destruindo a instância")

def criar_cachorro():
    c = Cachorro("Zeus" , "Branco e preto", False)
    print(c.nome)

criar_cachorro()
#c = Cachorro("Chappie", "amarelo")
#c.falar()

#del c