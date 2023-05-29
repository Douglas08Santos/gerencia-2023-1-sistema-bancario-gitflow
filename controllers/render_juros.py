from models.registros import contas
from models.conta_poupanca import Conta_poupanca

def render_juros(n_conta, taxa):
    print(f"Render Juros: {n_conta} \
          \nTaxa: {taxa}")

    # Verificar que o valor passado é negativo, 
    # se for a função se encerra
    if taxa < 0:
        print("Juros não realizado - taxa negativo")
        return False
    
    for conta in contas:
        if conta.n_conta == n_conta:
            if isinstance(conta, Conta_poupanca):
                print(f"Saldo anterior aos juros: {conta.saldo}")
                conta.renderJuros(taxa)
                print(f"Novo saldo: {conta.saldo}")
                return True
            else:
                print(f"Juros não adicionado - {n_conta} não é poupança")
    print("Juros não adicionado - Conta não cadastrada")
    return False