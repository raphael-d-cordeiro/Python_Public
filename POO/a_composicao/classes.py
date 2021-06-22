class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def cadastra_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_clientes(self):
        print(self.nome, self.idade)
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado