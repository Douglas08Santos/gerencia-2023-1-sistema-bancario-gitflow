from models.registros import contas
from models.conta import Conta

def cadastra_conta():
    print("Cadastro de conta")
    n_conta = input("Digite o numero da conta: ")
    saldo_inicial = float(input("Informe o saldo inicial da conta poupança:"))
    nova_conta = Conta(n_conta, saldo_inicial)
    

    if nova_conta not in contas:
        contas.append(nova_conta)
        print("Conta nova criada \
              \nConta: {}\
              \nSaldo: {}".format(nova_conta.n_conta,
                                  nova_conta.saldo))
    else:
        print("Numero de conta já utilizado anteriormente")
        