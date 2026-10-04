from models.estoque import Estoque
from models.pagamento import Avista, Parcelado
from models.pessoas import Pessoa
from models.venda import Venda
from views.console_view import ConsoleView


class VendaController:
    def __init__(self, view=None):
        self.view = view or ConsoleView()

    def realizar_venda(self):
        cliente_nome = self.view.digitar_texto("Digite o nome do cliente: ")
        cliente = next(
            (pessoa for pessoa in Pessoa.clientes if pessoa.nome == cliente_nome),
            None,
        )
        if cliente is None:
            self.view.mostrar_mensagem("Cliente não encontrado.", "vermelho")
            return

        vendedor_nome = self.view.digitar_texto("Digite o nome do vendedor: ")
        vendedor = next(
            (pessoa for pessoa in Pessoa.vendedores if pessoa.nome == vendedor_nome),
            None,
        )
        if vendedor is None:
            self.view.mostrar_mensagem("Vendedor não encontrado.", "vermelho")
            return

        venda = Venda(cliente, vendedor)
        while True:
            nome_produto = self.view.digitar_texto(
                "Qual o nome do produto que será comprado? "
            )
            produto = Estoque.buscar_produto(nome_produto)
            if produto is None:
                self.view.mostrar_mensagem("Produto não encontrado.", "vermelho")
                return

            quantidade = self.view.digitar_inteiro(
                "Quantos produtos serão comprados?", minimo=1
            )
            disponivel = produto._quantidade - venda.quantidade_do_produto(produto)
            if quantidade > disponivel:
                self.view.mostrar_mensagem(
                    "Não é possível comprar mais produtos do que o disponível "
                    "no estoque.",
                    "vermelho",
                )
            else:
                venda.adicionar_produto(produto, quantidade)
                self.view.mostrar_mensagem(
                    "Produto adicionado com sucesso!", "verde"
                )

            if self.view.adicionar_mais_produtos() != "1":
                break

        if not venda.produtos:
            return

        self.view.mostrar_resumo_venda(venda.produtos, venda.calcular_subtotal())
        while True:
            forma_pagamento = self.view.escolher_forma_pagamento()
            if forma_pagamento == "1":
                pagamento = Avista(venda.calcular_subtotal())
                break
            if forma_pagamento == "2":
                parcelas = self.view.digitar_inteiro("Quantas parcelas?", minimo=2)
                pagamento = Parcelado(venda.calcular_subtotal(), parcelas)
                break
            self.view.mostrar_mensagem("Opção Inválida.", "vermelho")

        self.view.mostrar_resumo_venda(
            venda.produtos,
            venda.calcular_subtotal(),
            pagamento.valor_total,
            parcelas=getattr(pagamento, "parcelas", None),
        )
        if self.view.confirmar_compra() == "1":
            venda.finalizar(pagamento.valor_total)
            self.view.mostrar_mensagem("Compra concluída com sucesso!", "verde")
        else:
            self.view.mostrar_mensagem("Compra cancelada.", "vermelho")

    def processar_devolucao_troca(self):
        cliente_nome = self.view.digitar_texto("Digite o nome do cliente: ")
        cliente = next(
            (pessoa for pessoa in Pessoa.clientes if pessoa.nome == cliente_nome),
            None,
        )
        if cliente is None:
            self.view.mostrar_mensagem("Cliente não encontrado.", "vermelho")
            return

        itens_elegiveis = []
        for compra in cliente.compras:
            for item in compra[0]:
                if (
                    item["quantidade_disponivel"] > 0
                    and Venda.esta_na_garantia(item)
                ):
                    itens_elegiveis.append((compra, item))

        if not itens_elegiveis:
            self.view.mostrar_mensagem(
                "O cliente não possui produtos dentro do prazo de garantia.",
                "vermelho",
            )
            return

        self.view.mostrar_itens_elegiveis(itens_elegiveis)
        indice = self.view.digitar_inteiro(
            "Digite o número do produto: ", minimo=1
        )
        if indice > len(itens_elegiveis):
            self.view.mostrar_mensagem("Produto inválido.", "vermelho")
            return

        compra, item = itens_elegiveis[indice - 1]
        quantidade = self.view.digitar_inteiro(
            "Quantas unidades deseja devolver ou trocar? ", minimo=1
        )
        if quantidade > item["quantidade_disponivel"]:
            self.view.mostrar_mensagem(
                "Quantidade maior do que a disponível para devolução ou troca.",
                "vermelho",
            )
            return

        operacao = self.view.escolher_operacao_devolucao()
        try:
            if operacao == "1":
                Venda.devolver_produto(compra, item, quantidade)
                self.view.mostrar_mensagem(
                    "Devolução realizada com sucesso!", "verde"
                )
            elif operacao == "2":
                Venda.trocar_produto(compra, item, quantidade)
                self.view.mostrar_mensagem("Troca realizada com sucesso!", "verde")
            else:
                self.view.mostrar_mensagem("Opção inválida.", "vermelho")
        except ValueError as erro:
            self.view.mostrar_mensagem(str(erro), "vermelho")
