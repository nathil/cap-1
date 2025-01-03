#5 - Considerando uma lista A, remova todos os itens repetidos.

#1o modo

print('primeiro modo\n')
lista = [3,6,7,8,5,4,2,3,6,4]
# resultado: [3,6,7,8,5,4,2]

repetidos = []
nao_repetidos = []

for valor in lista:
    if valor in nao_repetidos:
        repetidos.append(valor)
    else:
        nao_repetidos.append(valor)

print('Lista sem valores repetidos:', nao_repetidos)

#2o modo

print('\nSegundo modo\n')

nao_repetidos = list(set(lista))
print('Lista de valores não repetidos:', nao_repetidos)



