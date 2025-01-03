#2- Considerando as listas A e B, construa o conjunto de cada lista e informe se os conjuntos são disjuntos.

A = [9, 4, 6, 2, 0, 34, 5, 3, 55]
B = [19, 99, 4, 3, 5, 65, 45]


#1o modo
print('primeiro modo')

conjuntoA = set(A)
conjuntoB = set(B)

print(conjuntoA.isdisjoint(conjuntoB))


#2o modo
print('\nsegundo modoa\n')

conjuntoA = set()

for valor in A:
    conjuntoA.add(valor)

for valor in B:
    conjuntoB.add(valor)

print(conjuntoA)
print(conjuntoB)

print(conjuntoA.isdisjoint(conjuntoB))



