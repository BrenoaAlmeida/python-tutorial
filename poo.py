#Programação orientada a objetos
#Python é uma linguagem de programação multiparadigma.
#Trabalha com conceitos de classes e objetos.

class Veiculo:
    #Atributos da classe

    #Metodos
    #Usa se self, quando eu criar um objeto, baseado nessa clase, esse movimentar se refere esse objeto em particular
    #Não é necessario passar com o nome de self, é so uma convenção
    def movimentar(self):
        print("Movimentando o veiculo")

    #Metodo __init__ é o construtor da classe
    def __init__(self, fabricante, modelo):
        #Criação de atributos publicos
        self.fabricante = fabricante
        self.modelo = modelo
        #Criação de atributos privados (encapsulados)
        self.__cor = "vermelho"
        self.__ano = 2023
        self.__numero_registro = None
    
    #Getter
    def get_cor_ano(self):
        return print(f'Cor: {self.__cor}, Ano: {self.__ano}')
    
    def  get_numero_registro(self):
        return  print(f'Numero do registro: {self.__numero_registro}')
    
    #Setter
    def set_numero_registro(self, numero_registro):
        self.__numero_registro = numero_registro
        print(f'Numero do registro: {self.__numero_registro}')

#Herança
class Carro(Veiculo):
    #Metodo init sera herdado    

    def movimentar(self):
        print("Sou um carro")

#Polimorfismo
class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        #Classe  da qual Aviao herda
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print("Sou um aviao e me desloco pelo ceu")

if __name__ == "__main__":
    #Instanciando a classe
    meu_veiculo = Veiculo("Ford", "F-150")
    meu_veiculo.movimentar()

    carro = Carro("Chevrolet", "Onix")
    carro.movimentar()
    carro.get_cor_ano()
    print(meu_veiculo.modelo)

    aviao = Aviao("Boeing", "747", "Carga")
    aviao.movimentar()
    print(f'Categoria: {aviao.get_categoria()}')