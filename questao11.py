#11 - Considerando uma lista chamada PRODUCAO e um conjunto chamado BACKUP, verifique se o 
#backup está atualizado ou não. Caso esteja, informe que o backup está sincronizado, caso contrário, 
#sincronize o BACKUP e o exiba. Por mais que a produção possua itens repetidos, no backup basta uma 
#cópia de cada item.

producao = [1,4,5,7,5,4,7,9,8,4,5,6,8,6,3]
backup = {10,15,8,4}


#1o modo

print('primeiro modo\n')

conj_produção = set(producao)

if conj_produção == backup: 
    print('Backup está atualizado!')
else:
    backup = conj_produção

