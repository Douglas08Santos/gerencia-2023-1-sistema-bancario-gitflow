from models.registros import contas
from models.conta import Conta

def debito(n_conta, valor):
    print(f"Débito: {n_conta}")
    
    # Verificar que o valor passado é negativo, 
    # se for a função se encerra
    if valor < 0:
        print("Débito não realizado - Valor negativo")
        return False
    
    for conta in contas:
        if conta.n_conta == n_conta:
            if conta.saldo >= valor:
                print(f"Saldo anterior ao débito:\n{conta}")
                conta.debito(valor)
                print(f"Novo saldo:\n{conta}")
                return True
            else:
                print(f"Debito não contabilizado - Valor indisponível")
                return False
    print("Debito não contabilizado - Conta não cadastrada")
    return False