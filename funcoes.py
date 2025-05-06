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