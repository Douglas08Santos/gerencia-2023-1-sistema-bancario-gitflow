from models.conta import Conta

class Conta_poupanca(Conta):
    def __init__(self, n_conta, saldo_inicial):
        print('poupança')
        super().__init__(n_conta=n_conta)
        self.saldo = saldo_inicial

    def renderJuros(self, taxa:float):
        self.saldo += self.saldo * taxa/100
