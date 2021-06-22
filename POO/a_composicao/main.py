"""
Composição - A mais forte - A classe depende e mantem a outra classe...
 Essa relação é chamada de "TEM" (uma classe tem a outra).
 Aqui, a classe principal não funcionaria sem a outra e a outra nem existiria sem a classe principal.
 Quem cria e mantêm as referências das outras classes é a classe principal, portanto se ela deixar de existir,
 as outras também deixarão.
"""

from classes import Cliente
if __name__ == '__main__':
    cliente1 = Cliente('RAPHAEL', 31)
    cliente1.cadastra_endereco('SALTO', 'SP')
    cliente1.cadastra_endereco('INDAIATUBA', 'SP')
    cliente1.lista_clientes()
