from functools import reduce

#Funcoes são criadas usando a palavra-chave def, seguida pelo nome da função e parênteses.
#  exemplo def nome_da_funcao([argumentos]):
# Instruções

def funcao_hello_word():
    print("Hello Word")

def funcao_com_argumento(nome, email):
    print(f"Hello {nome} com email {email}")

def funcao_com_parametro_opcional(numero1 = 10, numero2 = 20):
    soma = numero1 + numero2
    print(f"A soma é {soma}")
    return soma

def funcao_com_parametro_nomeado(nome, email):
    print(f"Hello {nome} com email {email}")

def funcao_lambda():
    #Sintaxe:
    #lambda [argumentos]: expressão
    funcao = lambda x: x**2
    for i in range(1,11):
        print(funcao(i))

def funcao_map():
    #Sintaxe:
    #map(função, iterável)
    #Permite aplicar uma função a todos os elementos de um iterável (como listas, tuplas, etc.)
    #e retornar um novo iterável do tipo map com os resultados.
    numeros = [1, 2, 3, 4, 5]
    dobro = list(map(lambda x: x*2, numeros))
    print(dobro)

def funcao_filter():
    #Sintaxe:
    #filter(função, iterável)
    #Permite filtrar elementos de um iterável com base em uma função que retorna True ou False.
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)

def funcao_reduce():
    #Sintaxe:
    #reduce(função, iterável)
    #Permite aplicar uma função cumulativa a todos os elementos de um iterável,
    #reduzindo-o a um único valor.
    numeros = [1, 2, 3, 4, 5]
    soma = reduce(lambda x, y: x + y, numeros)    
    print(soma)
    total = reduce(lambda x, y: x**2 + y**2, numeros)
    print(total)

if __name__ == "__main__":
    funcao_com_parametro_nomeado(nome="Lucas", email="lucas@gmail.com")