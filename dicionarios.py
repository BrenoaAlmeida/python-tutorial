def executar():
    dicionario = {
        "nome": "Lucas",
        "idade": 20,
        "altura": 1.75
    }
    print(dicionario) #Mostra o dicionario
    print(dicionario["nome"]) #Mostra o valor da chave nome
    dicionario["peso"] = 70 #Adiciona o peso ao dicionario
    print(dicionario) #Mostra o dicionario com o peso adicionado
    del dicionario["peso"] #Remove o peso do dicionario
    print(dicionario) #Mostra o dicionario sem o peso
    print(dicionario.items()) #Mostra as chaves e valores do dicionario
    print(dicionario.keys()) #Mostra as chaves do dicionario
    print(dicionario.values()) #Mostra os valores do dicionario