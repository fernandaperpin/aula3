#Ex2
dicionario = {1: 'domingo',2:'segunda',3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sábado'}
usuario = int(input('Digite um número de 1 a 7: '))
if usuario <= 7 and usuario > 0:
    print(dicionario[usuario])
else:
        print('Número inválido')
