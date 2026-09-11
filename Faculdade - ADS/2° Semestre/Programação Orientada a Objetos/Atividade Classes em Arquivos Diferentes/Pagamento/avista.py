from pagamento import Pagamento

class Avista(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def realizar_pagamento(self):
        print(f"Pagamento realizado!\nTotal Pago: R${self.valor}")