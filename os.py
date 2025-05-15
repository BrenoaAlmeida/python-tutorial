import os
import pathlib
import shutil

def executar():
    diretorio_atual = os.getcwd() #Diretorio de trabalho atual
    diretorio_aberto = os.curdir() #Diretorio aberto
    conteudo_diretorio = os.listdir() #É possivel visualizar o conteudo de outro diretorio caso passe o caminho dele
    caminho_diretorio = ""
    novo_caminho_diretorio = os.chdir(caminho_diretorio) #Muda o diretorio atual
    arquivo = "arquivo.txt"
    caminho_para_arquivo = os.path.join(diretorio_atual, arquivo) #Cria o caminho para o arquivo
    #os.mkdir("Novo_Diretorio") #Cria um novo diretorio
    #os.rename("C\\Pasta", "C\\Pasta2") #Renomeia o diretorio
    #os.rmdir("C\\Pasta") #Remove o diretorio
    #os.makedirs("C:\\Pasta\\Subpasta") #Cria um novo diretorio e subdiretorio
    os.path.exists(caminho_para_arquivo) #Verifica se o caminho existe
    os.path.isdir(caminho_para_arquivo) #Verifica se o caminho é um diretorio
    os.path.isfile(caminho_para_arquivo) #Verifica se o caminho é um arquivo
    manipulador = open(caminho_para_arquivo, "x") #Abre o arquivo para escrita, passando parametro 'x' para criação
    nome_arquivo = os.path.basename(caminho_para_arquivo) #Retorna o nome do arquivo
    print(os.path.splitext(nome_arquivo)) #Retorna o nome do arquivo e a extensão

    #Biblioteca alternativa ao OS
    caminho = pathlib.Path(caminho_para_arquivo)
    caminho.cwd()

    shutil.rmtree("C:\\Pasta") #Remove o diretorio e todo o seu conteudo

    os.chdir("C:\\Pasta") #Muda o diretorio atual
    print(f'Diretorio atual: {os.getcwd()}')

    padrao_nome = input("Digite o padrão do nome do arquivo, sem extensão: ")
    for contador, arq, in enumerate(os.listdir()):
        if os.path.isfile(arq):
            nome_arquivo, extensao = os.path.splitext(arq)
            nome_arquivo = padrao_nome + ' ' + str(contador)
            nome_novo = f'{nome_arquivo}{extensao}'
            os.rename(arq, nome_novo)

    