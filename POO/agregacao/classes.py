class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def insere_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
