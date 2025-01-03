#3- Considerando as listas chaves e valores, construa um dicionário em que 
#cada elmento possui a chave e valor com os valores correspondentes das listas.

chaves = ['A', 'B', 'C', 'D', 'E']
valores = [19, 99, 4, 3, 5, 65, 45]


#1o modo
print('primeiro modo\n')


ABCDE = dict(zip(chaves, valores)) 

print(ABCDE)

#2o modo

print('\nsegundo modo\n')

ABCDE = {'A':19, 'B':99, 'C':4, 'D':3, 'E':5}

