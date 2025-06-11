from datetime import datetime
class Historico:
    def __init__(self):
        self._transacoes = []

    def addTransacoes(self, tipo, valor, contaDestino=none):
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now(),
            "conta_destino": contaDestino
        }
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
        extrato = []
        for transacao in self._transacoes:

            print(transacao)

            linha = {
                "data": transacao["data"].strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": transacao["tipo"],
                "valor": f"R$ {transacao['valor']:.2f}"
            }
            if transacao["conta_destino"]:
                linha["conta_destino"] = transacao["conta_destino"]
            extrato.append(linha)
        return extrato

            

