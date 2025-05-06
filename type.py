def executar():
    nome="Lucas"
    idade=20
    print(type(nome)) #A função type() mostra o tipo da variavel
    print(isinstance(nome, str)) #A função isinstance() mostra se a variavel é do tipo str
    print(type(nome) == str) #A função type() mostra o tipo da variavel
    print(isinstance(idade, (int, float))) #A função isinstance() mostra se a variavel é do tipo int ou float