from produto import Produto

if __name__ == '__main__':
    p1 = Produto('MOUSE', 'R$59.00')
    p1.desconto(10)
    print(p1.nome, p1.preco)