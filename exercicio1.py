def executar():
    explicacao="""Crie um script que peça para o usuario digitar o nome de 5  bebidas e armazene em uma lista. 
        Depois, imprima a lista na tela em ordem  alfabetica, um por linha usando um laço de repetição for. \n"""
    print(explicacao)
    
    bebidas = []
    for i in range(5):
        bebidas.append(input("Digite o nome de uma bebida: "))

    """
    Não é necessario criar uma nova  variavel para armazenar a lista ordenada,
    bebidas_ordenadas = sorted(bebidas) #Ordena a lista em ordem alfabetica
    """    

    bebidas.sort() #Ordena a lista em ordem alfabetica

    for bebida in bebidas:
        print(bebida) #Imprime a lista em ordem alfabetica