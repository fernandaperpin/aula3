#Ex3
import random as rd 
quantidade = int(input('Digite a quantidade de números que deseja na lista: '))
lista = []
linha = 1
if quantidade <= 0:
    print('Número inválido')
else:
    while linha <= quantidade:
        lista.append(rd.randrange(0,1000))
        linha+=1
    print('Lista: ', lista) 
    print('Maior valor: ', max(lista))
    print('Menor valor: ', min(lista))   