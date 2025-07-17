#Listas
frutas = ["laranja", "maca", "uva"]
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

print(letras)
print(numeros)
print(frutas)
print(carro)

print(frutas[-1])

numeros = [1,2,30,45,8,9,43]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

quadrado = [numero ** 2 for numero in numeros ]
print(quadrado)
print(pares)

#outra forma de fazer
#pares =[numero for numero in numeros if numero % 2  == 0]

linguagens = ["Python", "Java", "C", "C#"]
print(linguagens)
print(linguagens.index("Java"))
print(linguagens.pop())
print(linguagens)
print(linguagens.sort())
print(linguagens.sort(reverse=True))
print(linguagens.sort(key = lambda x: len(x)))
print(linguagens.sort(key = lambda x: len(x), reverse=True))
print(sorted(linguagens))

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])