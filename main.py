def helloWord():
    #This is my first python code
    print("Hello Word")
    nome="Lucas"
    print("Ola " + nome) #Concatenando string com variavel
    print("Ola " + nome + " Seja Bem Vindo") #Concatenando string com variavel
    print("Impede de Pular Linha", end="") #Imprime na mesma linha
    print(" Continuo na mes linha")
    print()
    print("Mensagem formatada pelo {0} que tem {1} anos".format(nome, 20)) #Usa o método .format() para substituir {} pelo valor de nome e 20    

#Variable
def testNomeVar():
    nome="Lucas"
    idade=20
    n1=n2=n3=n4=10 #É possivel incializar varias variaveis de uma vez
    nome2, idade2 = "Fabio", 17 #É possivel incializar varias variaveis de uma vez
    isSomething = True #Tipo booleano pode ser verdadeiro ou falso
    print(nome)
    print(idade)
    print(nome2)
    print(idade2)
    print(n1)

#Interpolação
def testInterpolacao():
    nome="Lucas"
    idade=20    
    print(f"Meu nome é {nome} e tenho {idade} anos")

def testType():
    nome="Lucas"
    idade=20
    print(type(nome)) #A função type() mostra o tipo da variavel
    print(isinstance(nome, str)) #A função isinstance() mostra se a variavel é do tipo str
    print(type(nome) == str) #A função type() mostra o tipo da variavel
    print(isinstance(idade, (int, float))) #A função isinstance() mostra se a variavel é do tipo int ou float

def testOperadores():
    soma = 5 + 5
    multiplicacao = 5 * 5
    divisao = 5 / 5
    divisaoInteira = 22 // 5 #Mostra o resultado inteiro da divisão
    subtracao = 5 - 5
    potencia = 5 ** 5
    resto = 5 % 2
    print(soma)
    print(multiplicacao)
    print(divisao)
    print(divisaoInteira)
    print(subtracao)
    print(potencia)
    print(resto)

def testInput():
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))
    soma = valor1 + valor2
    print(f"soma: {soma}")

def testComparacao():
    salario = 3000
    if(salario < 2000):
        print("Junior")
    elif(salario == 2000):
        print("Pleno")
    else:   
        print("Senior")

def testOperadoresLogicos():
    idade = 25
    altura = 1.75
    resultado = (idade >= 18) and (altura >= 1.70) #No Python é usado and, Or e not ao inves de &&, || e !
    msg = f"Pode participar {str(resultado)}"
    print(msg)
    resultado = not resultado #Invertendo valor do Resultado
    print(f"Resultado invertido: {resultado}")

def testCondicionais():
    media = 0.0
    n1 = int(input("Digite a nota 1: "))
    n2 = int(input("Digite a nota 2: "))
    media = (n1 + n2) / 2
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

def testFormat():
    salario = 3500.751254
    print("Seu salario é: {}".format(salario)) #Usa o método .format() para substituir {} pelo valor de salario.
    print(f"Salario formatado: {salario:.2f}") #formata para 2 casas decimais.
    print(f"Salario é \"{salario}\"") #Caractere de escape
    nome="Joao"
    idade=32
    print(f"Nome:\t{nome}\tIdade:\t{idade}") #Caractere de escape para tabulação(TAB)
    print("\\\\")

def testRepeticao():
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

    contador = 0
    for contador in range(1, 10):
        for contador_interno in range(1, 10):
            print(f"Contador: {contador} Contador Interno: {contador_interno}")            

def funcaoInterna():
    if __name__ == "__main__": #Funcao interna que verifica se o arquivo principal está sendo executado, verificando se a variavel internal  __name__  tem esse valor
        print("Executando o arquivo principal")

def testLists():
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

    planetas = list('Mercurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno') #Cria uma lista vazia, pode usar list() ou [] para criar a lista
    for planeta in planetas:
        print(planeta)

#Mesmas funções de uma lista, so que Tuplas são imutaveis
def testTupla():
    tupla = (2,4,6,8)
    print(tupla) #Mostra a tupla
    elementos = ('F', 'Cl', 'Br', 'I', 'At')
    print(elementos) #Mostra a tupla
    print(len(elementos)) #Mostra o tamanho da tupla
    print(elementos[0]) #Mostra o primeiro elemento da tupla

# helloWord()
# testNomeVar()
# testInterpolacao()
# testType()
# testOperadores()
# testInput()
# testComparacao()
# testOperadoresLogicos()
# testFormat()
#testRepeticao()
#funcaoInterna()
#testLists()

