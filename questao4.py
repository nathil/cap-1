#4 - Considerando uma lista A, informe a quantidade de itens repetidos.

lista = [3,6,7,8,5,4,2,3,6,4]

#1o modo
print('primeiro modo\n')
conjunto = set(lista)

print(conjunto)


repetidos = 0 

for valor in conjunto:
    frequencia = lista.count(valor)    
    print(frequencia)
    repetidos += frequencia-1

print(repetidos)

#2o modo

print('\nsegundo modo\n')


lista = [3,6,7,8,5,4,2,3,6,4]
semrepetidos = []
repetidos = []

for valor in lista:
    if valor in semrepetidos:
        repetidos.append(valor)
    else:
        semrepetidos.append(valor)
    
print('lista sem valores repetidos:', semrepetidos)
print('valores repetidos:', repetidos)
print('quantidade de valores repetidos:', len(repetidos))





