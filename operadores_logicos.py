def executar():
    idade = 25
    altura = 1.75
    resultado = (idade >= 18) and (altura >= 1.70) #No Python é usado and, Or e not ao inves de &&, || e !
    msg = f"Pode participar {str(resultado)}"
    print(msg)
    resultado = not resultado #Invertendo valor do Resultado
    print(f"Resultado invertido: {resultado}")

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

    salario = 3000
    if(salario < 2000):
        print("Junior")
    elif(salario == 2000):
        print("Pleno")
    else:   
        print("Senior")