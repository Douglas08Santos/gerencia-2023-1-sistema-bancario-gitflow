from models.registros import contas
from models.conta import Conta

def consulta_saldo(n_conta):
    print(f"Consulta de saldo da conta nº {n_conta}")
    for conta in contas:
        print(conta)
        if conta.n_conta == n_conta:
            print(f"Saldo: R$ {conta.saldo}")