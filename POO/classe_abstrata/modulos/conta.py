from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldoini, nome_cliente):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldoini
        self._nome_cliente = nome_cliente

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")

        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass
