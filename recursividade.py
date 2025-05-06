def executar():
    #Calcular o fatorial de um número
    n1 = int(input("Digite um número: "))
    fatorial = fatorial_recursivo(n1)
    print(f"O fatorial de {n1} é {fatorial}")

def fatorial_recursivo(n):    
    if n == 0 or n == 1:
        return 1    
    else:
        return n * fatorial_recursivo(n - 1)