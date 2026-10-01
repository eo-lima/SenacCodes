from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.devolucao import Devolucao


@dataclass
class Produto:
    codigo: str
    nome: str
    preco: Decimal
    estoque: int
    garantia_dias: int


@dataclass
class ItemVenda:
    produto: Produto
    quantidade: int
    preco_unitario: Decimal

    @property
    def subtotal(self) -> Decimal:
        return self.preco_unitario * self.quantidade


@dataclass
class Venda:
    numero: str
    data: date
    itens: list[ItemVenda]
    finalizada: bool = True
    devolucoes: list[Devolucao] = field(default_factory=list, init=False)