from modulos.cp import ContaPoupanca

if __name__ == '__main__':
    conta_poupanca = ContaPoupanca(1002, 153341, 5000, 'RAPHAEL D. CORDEIRO')
    conta_poupanca.consulta_saldo()
    conta_poupanca.depositar(1500)
    conta_poupanca.consulta_saldo()
    conta_poupanca.sacar(2000)
    conta_poupanca.consulta_saldo()