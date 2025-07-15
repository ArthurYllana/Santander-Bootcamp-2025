#Conjuntos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_c = {1, 2 ,3}
conjunto_d = {2, 3, 4}
conjunto_e = {4, 1, 3, 2 , 5, 6}

print(conjunto_c.difference(conjunto_d))
print(conjunto_d.difference(conjunto_c))
print(conjunto_c.issubset(conjunto_e))
print(conjunto_e.issubset(conjunto_c))
conjunto_a.remove(2)
print(conjunto_a)