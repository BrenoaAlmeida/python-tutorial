var_global = "Hello Word Global"

def executar():
    funcao_com_escopo_global()

def funcao_com_escopo_global():
    var_local = "Hello Word Local"
    print(f'var_local {var_local}')
    print(f'var_global {var_global}')

def modificar_var_global():
    global var_global
    var_global = "Hello Word Global Alterado"
    print(f'var_global {var_global}')

if __name__ == "__main__":
    # Isso não funciona, pois ao editar a var_global dentro de uma função 
    # o python cria uma variavel local com o nome de var_global
    var_global = "test"
    print(f'var_global {var_global}')
    #Para alterar a variavel global dentro de uma função, use a palavra-chave global
    modificar_var_global()
    print(f'var_global {var_global}')
    