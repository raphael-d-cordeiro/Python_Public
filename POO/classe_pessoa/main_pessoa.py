class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

if __name__ == '__main__':
    p1 = Pessoa.por_ano_nascimento('Raphael', 1990)
    #p1 = Pessoa('Raphael', 31)
    print(p1)
    print(p1.nome, p1.idade)
    p1.get_ano_nascimento()