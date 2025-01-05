#8- Considerando a lista A, exiba os elementos separados por _ (underline).

#1o modo

print('primeiro modo\n')

A = ['bola', 'boca', 'banana', 'bacaba', 'boi', 'bebida', 'baleia']

print(*A, sep = '_')

#2o modo

print('\nsegundo modo\n')

nova_listaA = '_'.join(map(str, A))
print(nova_listaA)


