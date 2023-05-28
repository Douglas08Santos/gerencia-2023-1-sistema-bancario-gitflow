from models.registros import contas
from models.conta import Conta
from controllers.credito import credito
from controllers.debito import debito
from controllers.consulta_saldo import consulta_saldo

def transferencia(n_conta_1, n_conta_2, valor):
    print(f"Transferência: {n_conta_1} => {n_conta_2}")
    
    # Verificar que o valor passado é negativo, 
    # se for a função se encerra
    if valor < 0:
        print("Transferência não realizada - Valor negativo")
        return False
    
    result_1 = False
    result_2 = False
    for conta in contas:
        if conta.n_conta == n_conta_1:
            result_1 = debito(n_conta_1, valor)
           
        if conta.n_conta == n_conta_2:
            result_2 = credito(n_conta_2, valor)
    
    # Confere o debito e o credito entre as conta foi realizado corretamente
    if result_1 == False:
        print(f"Transferencia não realizada - problema na conta {n_conta_1}")
        if result_2:
            debito(n_conta_2, valor)
        return False

    if result_2 == False:
        print(f"Transferencia não realizada - problema na conta {n_conta_2}")
        if result_1:
            credito(n_conta_1, valor)
            
        return False

    print("Transferencia realizada")
    return True