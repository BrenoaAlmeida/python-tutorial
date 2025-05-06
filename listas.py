def executar():    
    notas=[5,7,9,11,13]
    print(notas) #Mostra a lista
    notas2=[1,2,3,4,6]
    lista_notas=notas + notas2 #Concatena as listas
    print(lista_notas) #Mostra a lista concatenada
    print(notas[0]) #Mostra o primeiro elemento da lista
    print(notas[-1]) #Mostra o ultimo elemento da lista
    notas[0] = 10 #Altera o primeiro elemento da lista
    print(notas[0:2]) #Mostra os elementos da lista do indice 0 ao 2
    print(notas[:4]) #Mostra os elementos da lista do indice 0 ao 4
    print(len(notas)) #Mostra o tamanho da lista
    print(sorted(notas)) #Mostra a lista ordenada
    print(sum(notas)) #Mostra a soma dos elementos da lista
    print(min(notas)) #Mostra o menor elemento da lista
    print(max(notas)) #Mostra o maior elemento da lista
    lista_notas.append(33) #Adiciona um elemento no final da lista
    print(lista_notas) #Mostra a lista com o elemento adicionado
    lista_notas.pop()  #Remove o ultimo elemento da lista
    print(lista_notas) #Mostra a lista com o elemento removido
    lista_notas.remove(3) #Remove o elemento 3 da lista
    print(lista_notas) #Mostra a lista com o elemento removido
    lista_notas.insert(3, 10) #Adiciona o elemento 10 na posição 3 da lista
    print(f'Existe na lista: {13 in lista_notas}') #Verifica se o elemento 13 está na lista