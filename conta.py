from abc import ABC, abstractmethod

class Conta(ABC):
    _quant_contas = 0

    def __init__(self, agencia, titular):
        self._agencia = agencia
        self._numero = Conta.__calc_conta()
        self._titular = titular
        self._saldo = 0

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
        else:
            print("O valor não pode ser menor ou igual 0")
    
    def saque(self, valor):
        if valor>0 and valor <= self._saldo:
            self._saldo-=valor
        else:
            print("O valor deve ser maior que 0")
    
    def ver_saldo(self):
        print(f"O seu saldo é de R${self._saldo}")

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