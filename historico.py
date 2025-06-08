class Historico:
    def __init__(self):
        self._transacoes = []

    def addTransacoes(self, transacao):
        self._transacoes.append(transacao)

    def gerarExtrato(self):
        for transacao in self._transacoes:
            print(transacao)