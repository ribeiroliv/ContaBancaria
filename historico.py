class Historico:
    def __init__(self):
        self._transacoes = []

    def addTransacoes(self, transacao):
        self._transacoes.append(transacao)

#  def adicionar_transacao(self, tipo, valor):
#         data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         transacao = {
#             "tipo": tipo,
#             "valor": valor,
#             "data": data_hora
#         }
#         self.__transacoes.append(transacao)

    def gerarExtrato(self):
        for transacao in self._transacoes:
            print(transacao)

# def gerar_extrato(self, ultimas_n=10):
#         print("\n--- EXTRATO ---")
#         for transacao in self.__transacoes[-ultimas_n:]:
#             print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
#         print("---------------")