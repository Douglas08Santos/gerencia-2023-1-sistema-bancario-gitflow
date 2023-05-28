from models.registros import contas
from models.conta import Conta

def credito(n_conta, valor):
    print(f"Crédito: {n_conta}")

    # Verificar que o valor passado é negativo, 
    # se for a função se encerra
    if valor < 0:
        print("Crédito não realizado - Valor negativo")
        return False
    
    for conta in contas:
        if conta.n_conta == n_conta:
            print(f"Saldo anterior ao crédito: {conta.saldo}")
            conta.credito(valor)
            print(f"Novo saldo: {conta.saldo}")
            return True
    print("Crédito não adicionado - Conta não cadastrada")
    return False