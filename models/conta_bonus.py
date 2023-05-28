from models.conta import Conta

class Conta_bonus(Conta):
    def __init__(self, n_conta):
        print('bonus')
        super().__init__(n_conta=n_conta)
        self.pontuacao = int(10)

    # 0 - deposito, 1 - transferencia, 2 - devolução
    def credito(self, valor, flag=0):
        if flag == 0:
            print('deposito bonus')
            self.pontuacao += int(valor//100)
            return super().credito(valor)
        elif flag == 1:
            print('transferência bonus')
            self.pontuacao += int(valor//200)
            return super().credito(valor)
        
        return super().credito(valor)
    
    def __str__(self):
        return f"Numero da conta: {self.n_conta} \
            \nSaldo: {self.saldo} \
            \nPontuação: {self.pontuacao}"