from pagamento import Pagamento

class Parcelado(Pagamento):
    def __init__(self, valor, parcelas):
        self.valor = valor
        self.parcelas = parcelas

    def realizar_pagamento(self):
        print(f"Pagamento realizado!\nValor total: R${(self.valor*5)/100}\Número de Parcelas: {self.parcelas}\nValor por Parcela: {((self.valor*5)/100)/self.parcelas}")