from abc import ABC, abstractmethod
from historico import *

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
        return cls._quant_contas
    
   
        
    def deposito(self, valor):
        if valor>0:
            self._saldo+=valor
            self._historico.addTransacoes(f'Deposito: + R${valor:.2f}')
        else:
            print("O valor não pode ser menor ou igual 0")
    
    def saque(self, valor):
        if valor>0 and valor <= self._saldo:
            self._saldo-=valor
            self._historico.addTransacoes(f'Saque: - R${valor:.2f}')
        else:
            print("O valor deve ser maior que 0")
    

    
    def transferencia(self, valor, contaDestino):
        if self.saque(valor):
            contaDestino.deposito(valor)
            self


    @abstractmethod
    def manutencao(self):
        pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, titular):
        super().__init__(agencia, titular)

    def manutencao(self):
        self._saldo += self._saldo*0.005

class ContaCorrente(Conta):
    def __init__(self, agencia, titular):
        super().__init__(agencia, titular)

    def manutencao(self):
        self._saldo-=25
