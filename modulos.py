#Importando o modulo
#import math
#from math import * #Import universal que importa todos os metodos, permitindo usar somente o nome da  função

#Importa apenas metodo1
from math import pi
import random

#Import com alias
# import math as m

def executar():
    #Como importei o modulo math, posso usar as funções dele
    print(pi) #Mostra o valor de pi

    #Gera um valor aleatorio entre 1 e 20
    valor = random.randint(1, 20)
    print(valor)


    #Gera 5 valores aleatorios - int
    for i in range(5):
        n = random.randint(1, 50)
        print(f'Numero gerado: {n}')

        #Gera 5 valores aleatorios - float
    for i in range(5):
        n = random.random()
        print(f'Numero gerado: {round(n * 10, 2)}') #Arrendonda para 2 casas decimais

    valores = [1,2,3,4,5,6,7,8,9]
    valor_escolhido = random.sample(valores, 2) #Escolhe 2 valores aleatorios da lista
    print(f'Valores escolhidos: {valor_escolhido}') #Mostra os valores escolhidos

    valor_escolhido = random.sample(valores) #Escolhe 1 valor aleatorio da lista
    print(f'Valor escolhidos: {valor_escolhido}') #Mostra os valores escolhidos

    print(valores)
    valor_aleatorio = random.shuffle(valores) #Embaralha a lista
    print(f'Lista embaralhada: {valores}') #Mostra a lista embaralhada
