from math import sqrt

#Criando exceção personalizada
class NumeroNegativoError(Exception):
    #__init__ é o construtor da classe
    def __init__(self):
        pass #Ignore e passe adiante, como continue e break

def executar():
    n1 = 10
    n2 = 0

    try:
        r = round(n1 / n2, 2)
    #Caso não escreva o nome da exceção, o python irá capturar todas as exceções
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    #Caso não ocorra erro, execute o que esta dentro do bloco else
    else:
        print(f"Resultado: {r}")

def div(n1,n2):
    return round(n1 / n2, 2)

def RaiseException():
    try:
        n1 = int(input("Digite um número positivo: "))
        if n1 < 0:
            #raise é usado para lançar uma exceção
            raise NumeroNegativoError("Número negativo")
    except NumeroNegativoError:            
        raise print("Foi fornecido um número negativo")
    else:
        print(f"Raiz quadrada de {n1} é {sqrt(n1)}")            
    finally:
        print("Fim do programa")
        

if __name__ == "__main__":
    while True:
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            break
        except ZeroDivisionError:
            print("Divisão por zero não é permitida.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")        

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except:
        print(f"Ocorreu um erro inesperado")
    else:
        print(f"Resultado: {r}")
    #finally é executado independente de erro ou não
    finally:
        print("\nFim do programa")