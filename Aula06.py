cursor = "Python"

print(cursor.center(10, '#'))

print(".".join(cursor))

nome = "aRthuR"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!  "

print(texto + '.')
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')

nome= "Arthur"
idade = 20
profissao = "Programador"
linguagem = "Python e C#"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}." .format(linguagem, profissao, idade, nome))

#modo mais comum de ser usado 
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f'Valor de Pi: {PI:.2f}')
print(f"Valor de PI: {PI:10.2f}")

#fatiamento 

nome = "Guilherme Arthur de Carvalho"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])

#multiplas strings 

mensagem = f"""
    Olá meu nome é {nome}
    Eu estudou aprendendo PythonFinalizationError       
        Essa mensagem tem diferentes recursos 
"""