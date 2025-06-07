from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

if __name__ == "__main__":

    while True:
        try:
            op = input("""
                SELECIONE UMA OPÇÃO
                       1- CRIAR CONTA
                       2- ACESSAR CONTA
                       0- SAIR
            """)

            if op == 1:
                Cliente.cadastrar()
            elif op == 2:
                print("Acessando conta")
            elif op == 0:
                break
            else:
                print('Opção invalida!')
        except ValueError:
            print('Opção não encontrada')
            continue

