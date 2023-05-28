from models.registros import contas
from models.conta import Conta

def debito(n_conta, valor):
    print(f"Débito: {n_conta}")
    
    for conta in contas:
        if conta.n_conta == n_conta:
            print(f"Saldo anterior ao débito: {conta.saldo}")
            conta.debito(valor)
            print(f"Novo saldo: {conta.saldo}")
            return True
    print("Debito não contabilizado - Conta não cadastrada")
    return False