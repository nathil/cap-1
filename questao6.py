#6- Considerando uma lista A, construa um dicionário em que os valores do dicionário são: soma dos 
#elementos de A, maior elemnto de A, menor elemento de A, média dos elementos de A, lista A, lista A ordenada.

A = [19, 99, 4, 3, 5, 65, 45]

#1o modo

print('primeiro modo\n')

tam = len(A)
somaA = sum(A)
maiorValor = max(A)
menorValor = min(A)
media = somaA/tam
ordenadaA = sorted(A)

dic_A = {'Soma': somaA, 'Maior Valor': maiorValor, 'Menor Valor': menorValor, 'Média': media, 'Lista A': A, 
        'Lista Ordenada': ordenadaA}

print(dic_A)

#2o modo

print('\nsegundo modo')
cont = 0 
somaA = 0 
maiorValor = 0 
menorValor = 3333333

for i in A:
    cont += 1

for i in A:
    somaA = i + somaA

for i in A:
    if i > maiorValor:
        maiorValor = i 

for i in A:
    if i < menorValor:
        menorValor = i 

media = somaA/cont
ordenadaA = sorted(A)

chaves = ['Soma', 'Maior Valor', 'Menor Valor', 'Média', 'Lista A', 'Lista Ordenada']
valores = [somaA, maiorValor, menorValor, media, A, ordenadaA]

dic_A = dict(zip(chaves, valores))

print(dic_A)