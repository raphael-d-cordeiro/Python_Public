from .conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo, nome, limite_ini=100):
        super().__init__(agencia, conta, saldo, nome)
        self._limiteini = limite_ini

    def sacar(self, valor):
        if self._saldo + self._limiteini > 0:
            self._saldo -= valor
        else:
            print('Saldo insuficiente consulte seu gerente.')

    def consulta_saldo(self):
        print(f'Seu saldo atual é de: {self._saldo}')
