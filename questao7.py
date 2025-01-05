#7- Considerando as listas A e B, construa a lista C em que a primeira metade da lista C
#é igual a primeira metade da lista A e a segunda mentade da lista C é igual a segunda metdade da lista B.


#1o modo

print('primeiro modo\n')

A = ['bola', 'boca', 'banana', 'bacaba', 'boi', 'bebida', 'baleia']
B = ['casa', 'cola', 'caba', 'corda']

del A[3:]
del B[:2]

C = A + B

print(C)

#2o modo

print('\nsegundo modo\n')

A = ['bola', 'boca', 'banana', 'bacaba', 'boi', 'bebida', 'baleia']
B = ['casa', 'cola', 'caba', 'corda']

C = A[0:3] + B[2:4]

print(C)


