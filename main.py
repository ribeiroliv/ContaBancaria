from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

if __name__ == "__main__":

    while True:
        try:
            op = input("""
                SELECIONE UMA OPÇÃO
                       1- CADASTRAR CLIENTE
                       2- CRIAR CONTA --> CORRENTE
                       3- CRIAR CONTA --> POUPANÇA
                       4- REALIZAR DEPÓSITO
                       5- REALIZAR SAQUE
                       6- TRENSFERIR ENTRE CONTAS
                       7- EXIBIR TOTAL DE CLIENTES
                       0- SAIR
            """)

            if op == 1:
                Cliente.cadastrar()
            elif op == 2:
                Conta.criarCorrente()
            elif op == 3:
                Conta.criarPoupanca()
            elif op == 4:
                Conta.deposito()
            elif op == 5:
                Conta.saque()
            elif op == 6:
                Conta.tranferencia()
            elif op == 7:
                Conta.get_quant_contas()
            elif op == 0:
                break
            else:
                print('Opção invalida!')
        except ValueError:
            print('Opção não encontrada')
            continue

