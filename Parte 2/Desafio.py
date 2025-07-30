from abc import ABC, abstractmethod
from datetime import date

# ---------------------------
# Interface de Transação
# ---------------------------
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# ---------------------------
# Histórico de Transações
# ---------------------------
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

# ---------------------------
# Classe Conta
# ---------------------------
class Conta:
    def __init__(self, cliente, numero: int):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self) -> float:
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    def sacar(self, valor: float) -> bool:
        if valor <= 0 or valor > self.saldo:
            print("Saque inválido.")
            return False
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso.")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de depósito inválido.")
            return False
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")
        return True

# ---------------------------
# Conta Corrente
# ---------------------------
class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite: float, limite_saques: int):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

# ---------------------------
# Cliente
# ---------------------------
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        if conta in self.contas:
            sucesso = transacao.registrar(conta)
            if sucesso:
                conta.historico.adicionar_transacao(transacao)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

# ---------------------------
# Pessoa Física (herda Cliente)
# ---------------------------
class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# ---------------------------
# Transações Concretas
# ---------------------------
class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        return conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        return conta.sacar(self.valor)


# Criando cliente e conta
cliente = PessoaFisica(nome="Arthur", cpf="12345678900", data_nascimento=date(2000, 1, 1), endereco="Rua XPTO")
conta = ContaCorrente(cliente, numero=1, limite=500.0, limite_saques=3)
cliente.adicionar_conta(conta)

# Realizando transações
cliente.realizar_transacao(conta, Deposito(1000))
cliente.realizar_transacao(conta, Saque(200))
cliente.realizar_transacao(conta, Saque(100))

# Mostrando saldo e histórico
print(f"Saldo atual: R${conta.saldo_atual()}")
print("Histórico de transações:")
for t in conta.historico.transacoes:
    print(f"- {t.__class__.__name__}: R${t.valor}")
