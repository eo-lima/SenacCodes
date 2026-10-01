from collections.abc import Callable
from decimal import Decimal

from model.devolucao import Devolucao
from model.venda import ItemVenda, Venda


class TerminalView:
    def __init__(
        self,
        entrada: Callable[[str], str] | None = None,
        saida: Callable[[str], None] | None = None,
    ) -> None:
        self._entrada = entrada
        self._saida = saida or print

    def _perguntar(self, mensagem: str) -> str:
        if self._entrada is None:
            return input(mensagem)
        self._saida(mensagem)
        return self._entrada(mensagem)

    def exibir_menu(self) -> int:
        while True:
            self._saida("\n=== Casa & Conforto ===")
            self._saida("1 - Registrar devolução")
            self._saida("0 - Sair")
            try:
                opcao = int(self._perguntar("Escolha uma opção: "))
            except ValueError:
                self._saida("Digite 1 ou 0.")
                continue
            if opcao in (0, 1):
                return opcao
            self._saida("Opção inválida. Digite 1 ou 0.")

    def selecionar_itens(self, venda: Venda) -> list[tuple[ItemVenda, int]]:
        self._saida(f"\nItens da venda {venda.numero}:")
        for indice, item in enumerate(venda.itens, start=1):
            self._saida(
                f"{indice}. {item.produto.nome} - "
                f"{item.quantidade} un. - R$ {self._formatar_moeda(item.preco_unitario)}"
            )

        selecoes: list[tuple[ItemVenda, int]] = []
        for item in venda.itens:
            while True:
                try:
                    quantidade = int(
                        self._perguntar(
                            f"Quantidade de {item.produto.nome} a devolver "
                            "(0 para pular): "
                        )
                    )
                    break
                except ValueError:
                    self._saida("Digite uma quantidade inteira.")
            if quantidade != 0:
                selecoes.append((item, quantidade))
        return selecoes

    def exibir_comprovante(self, devolucao: Devolucao) -> None:
        self._saida("\n========== COMPROVANTE DE DEVOLUÇÃO ==========")
        self._saida(f"Devolução: {devolucao.numero}")
        self._saida(f"Venda: {devolucao.venda.numero}")
        self._saida(f"Data: {devolucao.data.strftime('%d/%m/%Y')}")
        for linha in devolucao.linhas:
            self._saida(
                f"{linha.item_venda.produto.nome} - {linha.quantidade} un. - "
                f"R$ {self._formatar_moeda(linha.subtotal)}"
            )
        self._saida(
            f"Valor estornado: R$ {self._formatar_moeda(devolucao.valor_estornado)}"
        )
        self._saida("===============================================")

    def exibir_mensagem(self, mensagem: str) -> None:
        self._saida(mensagem)

    @staticmethod
    def _formatar_moeda(valor: Decimal) -> str:
        return f"{valor:.2f}".replace(".", ",")