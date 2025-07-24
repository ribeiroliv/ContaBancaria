from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
from historico import Historico

if __name__ == "__main__":

    while True:
        try:
            print("""
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
            
            op = input("opção: ")

            if op == '1':
                Cliente.cadastrar()

            elif op == '2':
                Conta.criarConta()

            elif op == '3':
                numero_conta = input("Digite o número da conta: ")
                conta = Conta.carregar_conta(numero_conta)
                
                if conta:
                    conta.deposito()
                else:
                    print("Conta não encontrada!")

            elif op == '4':
                numero_conta = input("Digite o número da conta: ")
                conta = Conta.carregar_conta(numero_conta)
                
                if conta:
                    if isinstance(conta, ContaCorrente):
                        conta.saque()  # Chama o método de saque da ContaCorrente
                    else:
                        print("Saque disponível apenas para Conta Corrente.")
                else:
                    print("Conta não encontrada!")

            elif op == '5':
                numero_conta = input("Digite o número da conta: ")
                conta = Conta.carregar_conta(numero_conta)
                
                if conta:
                    conta.transferencia()
                else:
                    print("Conta não encontrada!")

            elif op == '6':
                Conta.get_quant_contas()

            elif op == '7':
                
                numero_conta = input("Digite o número da conta: ")
                conta = Conta.carregar_conta(numero_conta)
                
                if conta:
                    extrato = conta._historico.gerarExtrato()
                    if not extrato:
                        print("Nenhuma transação registrada.")
                    else:
                        print("\n=== EXTRATO ===")
                        for operacao in extrato:
                            destino = f" | Conta destino: {operacao['conta_destino']}" if 'conta_destino' in operacao else ""
                            print(f"{operacao['data']} | {operacao['tipo']} | Valor: {operacao['valor']}{destino}")
                else:
                    print("Conta não encontrada!")

            elif op == '0':
                print('Operações encerradas')
                break

            else:
                print('Opção invalida!')
                
        except ValueError:
            print('Opção não encontrada')
            continue

