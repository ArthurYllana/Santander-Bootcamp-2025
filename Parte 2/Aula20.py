class Estudante:
    escolaa = "DIO"  # variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome            # variável de instância
        self.matricula = matricula  # variável de instância

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {Estudante.escolaa}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Arthur", 1)
aluno_2 = Estudante("Guilherme", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_2.matricula = 3

mostrar_valores(aluno_2)
