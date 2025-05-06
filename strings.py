def executar():
    frase = "Meu nome é Lucas"
    email = "lucas@gmail.com"
    print(frase.split()) #Mostra a frase separada por espaço
    posicao = email.find('@') #Mostra a posição do @
    print(posicao) #Mostra a posição do @
    usuario = email[0:posicao] #Mostra o usuario
    dominio = email[posicao+1:] #Mostra o dominio
    print(f'Usuario: {usuario} Dominio: {dominio}') #Mostra o usuario e dominio
    print(frase.upper()) #Mostra a frase em maiusculo
    print(frase.lower()) #Mostra a frase em minusculo
    print(frase.title()) #Mostra a frase com a primeira letra maiuscula
    print(frase.capitalize()) #Mostra a frase com a primeira letra maiuscula
    frase= frase.replace("Lucas", "Joao") #Substitui Lucas por Joao
    print(frase) #Mostra a frase com a substituição
    frase_com_espaco = "   Olá Mundo   "
    print(frase_com_espaco.strip()) #Remove os espaços do inicio e do fim da string, também tem o lstrip() e rstrip()
    print(frase.startswith("Meu")) #Verifica se a string começa com "Meu"
    print(frase.endswith("Lucas")) #Verifica se a string termina com "Lucas"

    #formatação de strings
    salario = 3500.751254
    print("Seu salario é: {}".format(salario)) #Usa o método .format() para substituir {} pelo valor de salario.
    print(f"Salario formatado: {salario:.2f}") #formata para 2 casas decimais.
    print(f"Salario é \"{salario}\"") #Caractere de escape
    nome="Joao"
    idade=32
    print(f"Nome:\t{nome}\tIdade:\t{idade}") #Caractere de escape para tabulação(TAB)
    print("\\\\")

    #Interpolação basica
    nome="Lucas"
    idade=20    
    print(f"Meu nome é {nome} e tenho {idade} anos")