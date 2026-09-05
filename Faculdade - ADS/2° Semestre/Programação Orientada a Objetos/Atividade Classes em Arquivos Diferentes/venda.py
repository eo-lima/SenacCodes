from produtos import Produto
from Subpessoas.cliente import Cliente
from Subpessoas.vendedor import Vendedor

class Venda:
    def __init__(self, produtos: list, cliente: Cliente, vendedor: Vendedor):
        self.produtos = produtos
        self.cliente = cliente
        self.vendedor = vendedor

    def realizar_venda(self):
        print(f"Cliente: \n{self.cliente}")
        self.total = 0
        for produto in self.produtos:
            total = total + produto.preco
        print("Produtos: \n")
        for produto in self.produtos:
            print(produto.nome)
        print(f"Preço total: \nR${total}")
        print(f"Vendedor: {self.vendedor}")