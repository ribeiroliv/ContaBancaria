from abc import ABC, abstractmethod
from datetime import datetime
from historico import Historico
import bd2

class Conta(ABC):
    _quant_contas = 0

    def __init__(self, agencia, titular):
        self._agencia = agencia
        self._numero = Conta.__calc_conta()
        self._titular = titular
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def __calc_conta(cls):
        cls._quant_contas+=1
        return cls._quant_contas
    
    @classmethod
    def get_quant_contas(cls):
        return print( f' Quantidade de Contas: {cls._quant_contas}')
    
    @classmethod
    def criarConta(cls):
        print('--Criação de conta!--')
        try:
            clienteCPF = input('Digite seu cpf (Apenas números): ').strip()
            if not clienteCPF.isdigit() or len(clienteCPF) != 11:
                print('CPF inválido!')
                return None
            
            tipoConta = input('Qual tipo de conta? \n1-Corrente \n2-Poupança: ').strip()

            agencia = input('Número da agência').strip()

            bd2.cursor.execute("SELECT cpf FROM Clientes WHERE cpf = ?", (clienteCPF,))
            if not bd2.cursor.fetchone():
                print('Cliente não encontrado!')
                return None

            if tipoConta == '1':
                tipo = 'corrente'
                limite = 1000.00
                conta = ContaCorrente(agencia, clienteCPF, limite)
            elif tipoConta == '2':
                tipo = 'poupança'
                limite = None
                conta = ContaPoupanca(agencia, clienteCPF)
            else:
                print('Tipo de conta inválido!')
                return None
                
            bd2.cursor.execute("""
            INSERT INTO Contas(clienteCPF, tipo, agencia, saldo, limite, ativo)
            VALUES(?, ?, ?, ?, ?, ?)
        """, (clienteCPF, tipo, agencia, 0.0, limite, True))
            
            bd2.conn.commit()
            conta._numero = bd2.cursor.lastrowid #retorna o valor da última coluna autoincrementada inserida.

            print(f'\nConta criada com sucesso!')
            print(f'Número da conta: {conta._numero}')
            print(f'Agência: {agencia}')
            
            return conta

        except Exception as e:
            print(f'erro ao criar conta: {e}')
            bd2.conn.rollback()
            return False

    def deposito(self):
        print('--Depositando--')
        try:
            valor = float(input('Digite o valor a ser depositado: '))
            if valor > 0:
                bd2.cursor.execute("""
                        UPDATE Contas SET saldo = saldo + ? WHERE numero = ?
                    """, (valor, self._numero))
                    
                bd2.cursor.execute("""
                        INSERT INTO Historico (conta, tipooperacao, valor, datahorario)
                        VALUES (?, ?, ?, ?)
                    """, (self._numero, "Depósito", valor, datetime.now()))
                bd2.conn.commit()
                self._saldo += valor
                return True
        
        except Exception as e:
            print(f'Erro ao depositar: {e}')
            bd2.conn.rollback()
            return False

    @abstractmethod
    def saque(self):
        pass

    def transferencia(self):
        print('--Transferindo--')
        try:
            valor = float(input('Digite o valor a ser transferido: '))
            contaDestino = input('Digite o numero da conta destino: ')

            if valor <= 0:
                print('Valor deve ser positivo!')
                return False
            
            if valor > self._saldo:
                print('Saldo insuficiente!')
                return False
            if contaDestino == self._numero:
                print('Não pode transferir para a mesma conta!')
                return False
            
            bd2.cursor.execute("SELECT numero FROM Contas WHERE numero = ?", (contaDestino,))
            if not bd2.cursor.fetchone():
                print('Conta destino não encontrada!')
                return False

            bd2.cursor.execute("BEGIN TRANSACTION")

            # Atualiza saldo da conta de origem
            bd2.cursor.execute("""
                UPDATE Contas SET saldo = saldo - ? WHERE numero = ?
            """, (valor, self._numero))
            
            # Atualiza saldo da conta de destino
            bd2.cursor.execute("""
                UPDATE Contas SET saldo = saldo + ? WHERE numero = ?
            """, (valor, contaDestino))

                # Registra no histórico da conta de origem
            bd2.cursor.execute("""
                INSERT INTO Historico 
                (conta, tipooperacao, valor, contadestino, datahorario)
                VALUES (?, ?, ?, ?, ?)
            """, (self._numero, "Transferência enviada", -valor, contaDestino, datetime.now()))
            
            # Registra no histórico da conta de destino
            bd2.cursor.execute("""
                INSERT INTO Historico 
                (conta, tipooperacao, valor, contadestino, datahorario)
                VALUES (?, ?, ?, ?, ?)
            """, (contaDestino, "Transferência recebida", valor, self._numero, datetime.now()))

            bd2.conn.commit()
            self._saldo -= valor
            return True
        
        except Exception as e:
            print(f'Erro ao realizar transferencia: {e}')
            bd2.conn.rollback()
            return False

    @abstractmethod
    def manutencao(self):
        pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, titular):
        super().__init__(agencia, titular)

    def manutencao(self):
        rendimento = self._saldo * 0.005
        try:
            bd2.cursor.execute("""
                UPDATE Contas SET saldo = saldo + ? WHERE numero = ?
            """, (rendimento, self._numero))
            
            bd2.cursor.execute("""
                INSERT INTO Historico (conta, tipooperacao, valor, datahorario)
                VALUES (?, ?, ?, ?)
            """, (self._numero, "Rendimento", rendimento, datetime.now()))
            
            bd2.conn.commit()
            self._saldo += rendimento
            return True
        
        except Exception as e:
            print(f'Erro ao aplicar rendimento: {e}')
            bd2.conn.rollback()
            return False

class ContaCorrente(Conta):
    def __init__(self, agencia, titular, limite = 1000.00):
        super().__init__(agencia, titular)
        self._limite = limite

    @property
    def limite(self):
        return self._limite
    
    def manutencao(self):
        self._saldo-=25

    def saque(self):
        print('--Sacando--')
        try:

            valor = float(input('Digite o valor a ser sacado: '))

            if valor <= 0:
                print('Valor deve ser positivo!')
                return False
            
            if valor > (self._saldo + self._limite):
                print('Saldo insuficiente!')
                return False

            bd2.cursor.execute("""
                UPDATE Contas SET saldo = saldo - ? WHERE numero = ?
            """, (valor, self._numero))
            
            bd2.cursor.execute("""
                INSERT INTO Historico (conta, tipooperacao, valor, datahorario)
                VALUES (?, ?, ?, ?)
            """, (self._numero, "Saque", -valor, datetime.now()))
            
            bd2.conn.commit()
            self._saldo -= valor
            return True
            
        except Exception as e:
            print(f'Erro ao realizar saque: {e}')
            bd2.conn.rollback()
            return False