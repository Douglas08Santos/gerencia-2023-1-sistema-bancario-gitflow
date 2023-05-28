from models.registros import contas
from models.conta import Conta
from models.conta_bonus import Conta_bonus
from models.conta_poupanca import Conta_poupanca
from views.menu import menu_tipo_conta

def cadastra_conta():
    print("Cadastro de conta")
    n_conta = input("Digite o numero da conta: ")
    print(menu_tipo_conta)
    tipo_conta = 0

    while tipo_conta != '4':
        tipo_conta = input("Digite a opção do tipo de conta:")
        if tipo_conta == '1':
            nova_conta = Conta(n_conta)
            tipo_conta = '4'
        elif tipo_conta == '2':
            nova_conta = Conta_bonus(n_conta)
            tipo_conta = '4'
        elif tipo_conta == '3':
            nova_conta = Conta_poupanca(n_conta)
            tipo_conta = '4'
        else:
            print('opção invalida')

    if nova_conta not in contas:
        contas.append(nova_conta)
        print(nova_conta)
    else:
        print("Numero de conta já utilizado anteriormente")
        