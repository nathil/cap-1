#10- Considerando o dicionário D, remova o elemento com a cahve nome e exiba o dicionário atualizado.

#1o modo

print('primeiro modo\n')

D = {'nome': 'Renato Hidaka Torres', 'e-mail': 'renatohidaka@ufpa.br', 'ID': '123'}

D.pop('nome')

print(D)

#2o modo

print('\nsegundo modo\n')

D = {'nome': 'Renato Hidaka Torres', 'e-mail': 'renatohidaka@ufpa.br', 'ID': '123'}

del D['nome']

print(D)


