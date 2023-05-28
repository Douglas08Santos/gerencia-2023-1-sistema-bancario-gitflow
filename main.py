from controllers.cadastro_conta import cadastra_conta
from controllers.consulta_saldo import consulta_saldo
from views.menu import menu
from models.conta import Conta


def main():
    opcao = 0

    while opcao != 4:
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
            print("Saindo...")
        else:
            print("Opção digitada incorretamente")
    return 0

if __name__ == "__main__":
    main()