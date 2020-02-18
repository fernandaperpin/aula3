import random as rd 
quantidade = int(input('Digite um valor inteiro: '))
lista = []
linha = 1
if quantidade <= 0:
    print('Número inválido')
else:
    while linha <= quantidade:
        lista.append(rd.randrange(0,1000))
        print(lista)
        linha+=1  