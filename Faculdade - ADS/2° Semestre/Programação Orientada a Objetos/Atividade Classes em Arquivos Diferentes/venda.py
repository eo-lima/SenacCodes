from produtos import Produto
from Subpessoas.cliente import Cliente
from Subpessoas.vendedor import Vendedor

class Venda:
    def __init__(self, produtos: list, cliente: Cliente, vendedor: Vendedor):
        self.produtos = produtos
        self.cliente = cliente
        self.vendedor = vendedor

    def realizar_venda(self):
        self.total = 0
        for produto in self.produtos:
            total = total + produto.preco
            