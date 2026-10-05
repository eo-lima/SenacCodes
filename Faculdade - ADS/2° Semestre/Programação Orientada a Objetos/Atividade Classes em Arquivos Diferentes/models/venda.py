class Venda:
    def __init__(self, cliente, vendedor):
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append({"produto": produto, "quantidade": quantidade})

    def quantidade_do_produto(self, produto):
        return sum(
            item["quantidade"]
            for item in self.produtos
            if item["produto"] is produto
        )

    def calcular_subtotal(self):
        return sum(
            item["produto"]._preco * item["quantidade"]
            for item in self.produtos
        )

    def finalizar(self, valor_total):
        for item in self.produtos:
            produto = item["produto"]
            quantidade = item["quantidade"]
            produto._quantidade -= quantidade
            self.vendedor._comissao += (
                produto._preco * quantidade * produto.comissao
            )
        self.cliente.compras.append([self.produtos.copy(), valor_total])
