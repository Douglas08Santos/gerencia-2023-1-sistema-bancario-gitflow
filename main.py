from controllers.cadastro_conta import cadastra_conta
from controllers.consulta_saldo import consulta_saldo
from controllers.credito import credito
from controllers.debito import debito
from controllers.transferencia import transferencia
from views.menu import menu

from models.registros import mostrar_contas


def main():
    opcao = 0

    while opcao != 7:
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
            n_conta = input("Digite o numero da conta que deseja sacar? [somente números]: ")
            valor = float(input("Digite o valor que deseja sacar da conta? [somente números]: "))
            debito(n_conta, valor)
        elif opcao == 6:
            n_conta_1 = input("Digite o numero da conta de origem da transferência? [somente números]: ")
            n_conta_2 = input("Digite o numero da conta de destino da transferência? [somente números]: ")
            valor = float(input("Digite o valor que deseja transferir da conta? [somente números]: "))
            transferencia(n_conta_1, n_conta_2, valor)
        elif opcao == 7:
            print("Saindo...")

        else:
            print("Opção digitada incorretamente")
    return 0

if __name__ == "__main__":
    main()