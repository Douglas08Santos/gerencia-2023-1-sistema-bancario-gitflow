from models.registros import contas
from models.conta import Conta

def credito(n_conta, valor):
    print(f"Crédito: {n_conta}")
    
    for conta in contas:
        if conta.n_conta == n_conta:
            print(f"Saldo anterior ao crédito: {conta.saldo}")
            conta.credito(valor)
            print(f"Novo saldo: {conta.saldo}")
            return True
    print("Crédito não adicionado - Conta não cadastrada")
    return False