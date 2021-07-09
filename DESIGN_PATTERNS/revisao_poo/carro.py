from datetime import datetime


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__nascimento = datetime.now()

    @property
    def nome(self):
        return self.__nome

    def __str__(self) -> str:
        return f'{self.nome}'


class Carro:

    def __init__(self, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.motorista = None

    @property
    def motorista(self):
        return self.__motorista

    @motorista.setter
    def motorista(self, pessoa: Pessoa):
        self.__motorista = pessoa

    def dirigir(self) -> None:
        self.acelerar(1)

    def __str__(self) -> str:
        if hasattr(self.__motorista, 'nome'):
            return f'Carro do (a) {self.__motorista.nome}'
        return 'Carro sem motorista'

    def acelerar(self, velocidade: int) -> None:
        self.__velocidade += velocidade

    def parar(self) -> None:
        self.__velocidade = 0


if __name__ == '__main__':
    pessoa = Pessoa(nome='Raphael')
    print(pessoa)
    fusca = Carro()
    print(fusca)
    fusca.motorista = pessoa
    print(fusca)
    fusca.dirigir()
    fusca.acelerar(10)
    fusca.parar()
    print(fusca.__dict__)
