class Conta:
    def __init__(self, n_conta, saldo_inicial):
        self.n_conta = n_conta
        self.saldo = saldo_inicial

    def credito(self, valor):
        self.saldo += valor
    
    def debito(self, valor):
        self.saldo -= valor
    
    def __eq__(self, other):
        if isinstance(other, Conta):
            return self.n_conta == other.n_conta

    def __str__(self):
        return f"Numero da conta: {self.n_conta}\nSaldo: {self.saldo}"