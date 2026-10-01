from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from model.venda import ItemVenda, Venda


@dataclass
class LinhaDevolucao:
    item_venda: ItemVenda
    quantidade: int

    @property
    def subtotal(self) -> Decimal:
        return self.item_venda.preco_unitario * self.quantidade


@dataclass
class Devolucao:
    """Associa a devolução à venda original, que pode ter várias devoluções parciais."""

    numero: int
    venda: Venda
    data: date
    linhas: list[LinhaDevolucao]
    valor_estornado: Decimal

    @classmethod
    def registrar(
        cls,
        venda: Venda,
        selecoes: list[tuple[ItemVenda, int]],
        data_devolucao: date,
    ) -> Devolucao:
        if not venda.finalizada:
            raise ValueError("A devolução só pode ser feita para uma venda finalizada.")
        if data_devolucao < venda.data:
            raise ValueError("A data da devolução não pode ser anterior à venda.")
        if not selecoes:
            raise ValueError("Selecione ao menos um item para devolver.")

        itens_escolhidos = [item for item, _ in selecoes]
        if len({id(item) for item in itens_escolhidos}) != len(itens_escolhidos):
            raise ValueError("Cada item da venda deve aparecer apenas uma vez.")

        linhas: list[LinhaDevolucao] = []
        for item, quantidade in selecoes:
            if not any(item is item_venda for item_venda in venda.itens):
                raise ValueError("O item selecionado não pertence a esta venda.")
            if quantidade <= 0:
                raise ValueError("A quantidade devolvida deve ser maior que zero.")

            quantidade_devolvida = sum(
                linha.quantidade
                for devolucao in venda.devolucoes
                for linha in devolucao.linhas
                if linha.item_venda is item
            )
            disponivel = item.quantidade - quantidade_devolvida
            if quantidade > disponivel:
                raise ValueError(
                    f"Quantidade inválida para {item.produto.nome}: "
                    f"restam {disponivel} item(ns) para devolução."
                )

            dias_desde_a_venda = (data_devolucao - venda.data).days
            if dias_desde_a_venda > item.produto.garantia_dias:
                raise ValueError(
                    f"O prazo de garantia de {item.produto.nome} expirou."
                )
            linhas.append(LinhaDevolucao(item, quantidade))

        total = sum((linha.subtotal for linha in linhas), Decimal("0.00"))
        devolucao = cls(
            numero=len(venda.devolucoes) + 1,
            venda=venda,
            data=data_devolucao,
            linhas=linhas,
            valor_estornado=total,
        )

        for linha in linhas:
            linha.item_venda.produto.estoque += linha.quantidade
        venda.devolucoes.append(devolucao)
        return devolucao