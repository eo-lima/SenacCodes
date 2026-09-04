produtos = []

class Produto:
    def __init__(self, preco, quantidade, garantia):
        self._preco = preco
        self._quantidade = quantidade
        self._garantia = garantia