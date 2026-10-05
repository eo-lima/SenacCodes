class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor_total(self):
        return self.valor


class Avista(Pagamento):
    pass


class Parcelado(Pagamento):
    def __init__(self, valor, parcelas):
        super().__init__(valor)
        self.parcelas = parcelas

    @property
    def valor_total(self):
        return self.valor * 1.1
