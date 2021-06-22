"""
Agregação - Algo mais forte - A classe depende da outra classe... Essa relação é chamada de "TEM" ou "USA"
(uma classe tem ou usa a outra). Aqui, a classe principal não funcionaria sem a outra, porque a parte principal
dela depende da(s) outra(s) classe(s).

"""

from classes import CarrinhoDeCompras, Produto

if __name__ == '__main__':
    carrinho = CarrinhoDeCompras()
    p1 = Produto('IPHONE', 8000)
    p2 = Produto('PC', 5200)
    p3 = Produto('TV', 2900)
    p4 = Produto('LIQUIDIFICADOR', 55)
    carrinho.insere_produto(p1)
    carrinho.insere_produto(p2)
    carrinho.insere_produto(p3)
    carrinho.insere_produto(p4)
    carrinho.lista_produtos()
