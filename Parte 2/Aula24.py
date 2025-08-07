import functools

# Decorador que executa algo antes e depois da função
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)  # agora armazena o retorno
        print("Faz algo depois de executar")
        return resultado  # agora existe e é retornado corretamente

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return f"Argumento extra: {outro_argumento}"  # retorna algo

resultado = ola_mundo("João", 1000)
print(resultado)

# Decorador que duplica a execução e retorna o segundo resultado
def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)  # chamada apenas para exibir
        return func(*args, **kwargs)  # valor final retornado

    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)
