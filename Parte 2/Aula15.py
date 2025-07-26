#Herança Múltipla 

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

class Mamifero (Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return "Mamifero"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "Ave"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, **kw):
        super().__init__(cor_pelo, **kw)

    def __str__(self):
        return "Ornintorrinco"

gato = Gato(cor_pelo="Preto", nro_patas=4)
print(gato)

ornitorrinco = Ornitorrinco(cor_pelo="Marrom", cor_bico="Laranja", nro_patas=2)
print(ornitorrinco)
