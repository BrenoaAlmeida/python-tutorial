def executar():
    """"    
    Função interna que verifica se o arquivo principal está sendo executado, 
    verificando se a variavel internal  __name__  tem esse valor
    """
    if __name__ == "__main__":
        print("Executando o arquivo principal")