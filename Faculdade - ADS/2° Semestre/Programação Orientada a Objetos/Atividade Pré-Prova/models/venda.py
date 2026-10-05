from datetime import date, timedelta


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
        subtotal = self.calcular_subtotal()
        fator_pagamento = valor_total / subtotal if subtotal else 1
        produtos_historico = []

        for item in self.produtos:
            produto = item["produto"]
            quantidade = item["quantidade"]
            produto._quantidade -= quantidade
            self.vendedor._comissao += (
                produto._preco * quantidade * produto.comissao
            )
            item_historico = item.copy()
            item_historico.update(
                {
                    "data_venda": date.today(),
                    "quantidade_disponivel": quantidade,
                    "valor_unitario_venda": (
                        produto._preco * fator_pagamento
                    ),
                    "comissao_unitaria": produto._preco * produto.comissao,
                    "vendedor": self.vendedor,
                }
            )
            produtos_historico.append(item_historico)

        self.cliente.compras.append([produtos_historico, valor_total])

    @staticmethod
    def esta_na_garantia(item, hoje=None):
        data_venda = item.get("data_venda")
        if data_venda is None:
            return False

        hoje = hoje or date.today()
        fim_garantia = data_venda + timedelta(
            days=item["produto"]._garantia
        )
        return data_venda <= hoje <= fim_garantia

    @staticmethod
    def devolver_produto(compra, item, quantidade):
        if not Venda.esta_na_garantia(item):
            raise ValueError("O produto está fora do prazo de garantia.")
        if quantidade > item["quantidade_disponivel"]:
            raise ValueError("Quantidade maior do que a disponível para devolução.")

        item["quantidade_disponivel"] -= quantidade
        item["produto"]._quantidade += quantidade
        compra[1] -= item["valor_unitario_venda"] * quantidade
        item["vendedor"]._comissao -= item["comissao_unitaria"] * quantidade

    @staticmethod
    def trocar_produto(compra, item, quantidade):
        if not Venda.esta_na_garantia(item):
            raise ValueError("O produto está fora do prazo de garantia.")
        if quantidade > item["quantidade_disponivel"]:
            raise ValueError("Quantidade maior do que a disponível para troca.")

        produto = item["produto"]
        if produto._quantidade < quantidade:
            raise ValueError("Não há unidades suficientes para realizar a troca.")

        item["quantidade_disponivel"] -= quantidade
        produto._quantidade -= quantidade

        produto_trocado = item.copy()
        produto_trocado["quantidade"] = quantidade
        produto_trocado["quantidade_disponivel"] = quantidade
        compra[0].append(produto_trocado)
