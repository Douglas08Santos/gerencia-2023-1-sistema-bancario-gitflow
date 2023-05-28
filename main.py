from controllers.cadastro_conta import cadastra_conta
from controllers.consulta_saldo import consulta_saldo
from controllers.credito import credito
from views.menu import menu
from models.conta import Conta

from models.registros import mostrar_contas


def main():
    opcao = 0

    while opcao != 5:
        print(menu)
        opcao = int(input("Qual sua opção desejada? "))
        if opcao == 1:
            cadastra_conta()
        elif opcao == 2:
            mostrar_contas()
        elif opcao == 3:
            n_conta = input("Digite o numero da conta que deseja ver o saldo? [somente números]: ")
            consulta_saldo(n_conta)
        elif opcao == 4:
            n_conta = input("Digite o numero da conta que deseja depositar? [somente números]: ")
            valor = float(input("Digite o valor que deseja depositar na conta? [somente números]: "))
            credito(n_conta, valor)
        elif opcao == 5:
            print("Saindo...")

        else:
            print("Opção digitada incorretamente")
    return 0

if __name__ == "__main__":
    main()