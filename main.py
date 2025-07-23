from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
import historico

if __name__ == "__main__":

    while True:
        try:
            op = input("""
                SELECIONE UMA OPÇÃO
                       1- CADASTRAR CLIENTE
                       2- CRIAR CONTA 
                       3- REALIZAR DEPÓSITO
                       4- REALIZAR SAQUE
                       5- TRENSFERIR ENTRE CONTAS
                       6- EXIBIR TOTAL DE CLIENTES
                       7- VER EXTRATO
                       0- SAIR
            """)

            if op == '1':
                Cliente.cadastrar()
            elif op == '2':
                Conta.criarConta()
            elif op == '3':
                Conta.deposito()
            elif op == '4':
                ContaCorrente.saque()
            elif op == '5':
                Conta.tranferencia()
            elif op == '6':
                Conta.get_quant_contas()
            elif op == '7':
                historico.gerarExtrato()
            elif op == '0':
                break
            else:
                print('Opção invalida!')
        except ValueError:
            print('Opção não encontrada')
            continue

