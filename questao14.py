#14 - Considerando uma lista chamada PRODUCAO e um conjunto chamado BACKUP, informe os itens da PRODUCAO que 
#já estão no BACKUP.

#1o modo

print('primeiro modo\n')

producao = [1,4,5,7,5,4,7,9,8,4,5,6,8,6,3]
backup = {10,15,8,4}

conj_producao = set(producao)

print('Os elementos presentes em produção que já estão em backup são:', conj_producao & backup)

#2o modo

print('\nsegundo modo\n')

producao = [1,4,5,7,5,4,7,9,8,4,5,6,8,6,3]
backup = {10,15,8,4}

conj_producao = set(producao)

print('Os elementos presentes em produção que já estão em backup são:', conj_producao.intersection(backup))