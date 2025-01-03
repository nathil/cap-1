#1- Considerando as listas A, B, C e D, construa um dicionário com quatro elementos 
# em que o valor da cada elemento corresponde a soma dos valores de cada lista. 
# A chave dos elementos devem ser, respectivamente, as strings 'A', 'B', 'C' e 'D'.

#pegando os valores de cada lista
A = [1,5,4,7,8,6,5,8,9]
B = [10,32, 1, 1, 1]
C = [9, 4, 6, 2, 0, 34, 5, 3, 55]
D = [19, 99, 4, 3, 5, 65, 45]

#fazendo a soma total dos valores
somaA = sum(A)
somaB = sum(B)
somaC = sum(C)
somaD = sum(D)

#1o modo
print('primeiro modo \n')

#transformando em dicionário
ABCD = {'A': somaA, 'B': somaB, 'C': somaC, 'D': somaD}

print(ABCD)


#2o modo
print('\n2o modo \n')

#criar as chaves
chaves = ['A', 'B', 'C', 'D']

#transformar as somas em valores 
valores = [somaA, somaB, somaC, somaD ]

#tranformando tudo em um dicionário
ABCD = dict(zip(chaves, valores))
print(ABCD)




