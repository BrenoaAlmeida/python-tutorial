import declaracao_variavies
import dicionarios
import docstring
import exercicio1
import funcao_interna
import inputs
import listas
import matematica
import modulos
import operadores_logicos
import operadores
import primeiro_codigo
import repeticoes
import strings
import tuplas
import type
import escopos
import execoes
import recursividade


opcoes = {
    "1": lambda: declaracao_variavies.executar(),
    "2": lambda: dicionarios.executar(),
    "3": lambda: docstring.executar(),
    "4": lambda: exercicio1.executar(),
    "5": lambda: funcao_interna.executar(),
    "6": lambda: inputs.executar(),
    "7": lambda: listas.executar(),
    "8": lambda: matematica.executar(),
    "9": lambda: modulos.executar(),
    "10": lambda: operadores_logicos.executar(),
    "11": lambda: operadores.executar(),
    "12": lambda: primeiro_codigo.executar(),
    "13": lambda: repeticoes.executar(),
    "14": lambda: strings.executar(),
    "15": lambda: tuplas.executar(),
    "16": lambda: type.executar(),
    "17": lambda: escopos.executar(),
    "18": lambda: execoes.executar(),
    "19": lambda: recursividade.executar()
}

# Loop de menu
while True:    
    print("\nEscolha uma opção: ")
    print("Opções disponíveis:")
    print("1 - Declaracao de Variáveis")
    print("2 - Dicionários")
    print("3 - DocString")
    print("4 - Exercício 1")
    print("5 - Função Interna")
    print("6 - Input")
    print("7 - Listas")
    print("8 - Matemática")
    print("9 - Módulos")
    print("10 - Operadores Lógicos")
    print("11 - Operadores")
    print("12 - Primeiro Código")
    print("13 - Repetições")
    print("14 - Strings")
    print("15 - Tuplas")
    print("16 - Type")
    print("17 - escopos")
    print("18 - Exceções")
    print("19 - Recursividade")

    print("99 - sair\n")
    escolha = input()
    print()
    
    if escolha.lower() == "99":
        print("Saindo...")
        break

    acao = opcoes.get(escolha)
    if acao:
        acao()
    else:
        print("Opção inválida. Tente novamente.")