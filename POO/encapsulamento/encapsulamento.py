'''
public, protected e private
_ = protected coloca o atributo como privado, mas ainda acessivel publicamente
__ = private força o atributo ser totalmente privado
'''


class BancoDeDados:
    def __init__(self):
        self.__dados = {}

    def insere_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


if __name__ == '__main__':
    bd = BancoDeDados()
    bd.insere_clientes(1, 'Raphael')
    bd.insere_clientes(2, 'Douglas')
    bd.insere_clientes(3, 'Cordeiro')
    bd.__dados = 'teste'
    print(bd.__dados) # se tentarmos alterar o atributo totalmente private
    # o python cria um novo atributo renomeando o anterior da classe
    # para evitar isso tambem, devemos criar um @property para o atributo sem o setter
    print(bd._BancoDeDados__dados) # Então para acessarmos o atributo do construtor
    #da classe utilisamos instancia.NomeDaClasse__nomedoatributo
    bd.lista_clientes()
