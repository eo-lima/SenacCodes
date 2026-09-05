produtos = []

class Produto:
    def __init__(self, nome, preco, quantidade, garantia):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._garantia = garantia