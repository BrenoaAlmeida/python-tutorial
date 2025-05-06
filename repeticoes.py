def executar():
    #Repetição com for
    planetas = list('Mercurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno') #Cria uma lista vazia, pode usar list() ou [] para criar a lista
    for planeta in planetas:
        print(planeta)

    #Repetição com while
    while True:
        print("Digite seu nome ou x para sair: ")
        nome = input()
        print(f"bem vindo {nome}")
        if nome == "x" or nome == "X":
            break #Saindo do loop
    lista = [1,2,3,4,5] 
    for item in lista:
        print(item)
    palavra = "Boson"
    for letra in palavra:
        print(letra)
    for numero in range(1, 9): #É um alcançe de valores, de X até Y, nesse caso gera numero de 1 até 8
        print(f'\n{numero}')
    for letra in palavra:
        if letra == "o":
            continue #Encerra a iteração atual e continua para a próxima
    
    print("Repetição Alinhada")
    contador = 0
    for contador in range(1, 10):
        for contador_interno in range(1, 10):
            print(f"Contador: {contador} Contador Interno: {contador_interno}")            
