#9- Considerando a lista A,
# utilize slice para exibir os dois primeiros e os dois últimos elementos da lista.

A = ['bola', 'boca', 'banana', 'bacaba', 'boi', 'bebida', 'baleia']

#1o modo

print('primeiro modo\n')

print(A[0:2] + A[5:7])

#2o modo 

print('\nsegundo modo\n')

print(A[0:2] + A[-2:])
