from datetime import date
from decimal import Decimal

from controller.devolucao_controller import DevolucaoController
from model.venda import ItemVenda, Produto, Venda
from view.terminal import TerminalView


def main() -> None:
    chaleira = Produto("P001", "Chaleira elétrica", Decimal("129.90"), 4, 30)
    torradeira = Produto("P002", "Torradeira", Decimal("89.90"), 2, 15)
    venda = Venda(
        numero="V-2026-014",
        data=date(2026, 9, 10),
        itens=[
            ItemVenda(chaleira, quantidade=2, preco_unitario=chaleira.preco),
            ItemVenda(torradeira, quantidade=1, preco_unitario=torradeira.preco),
        ],
    )

    respostas = iter(["1", "1", "0"])
    view = TerminalView(entrada=lambda _mensagem: next(respostas))
    controller = DevolucaoController(view)
    devolucao = controller.executar(venda, data_devolucao=date(2026, 9, 30))

    assert devolucao is not None
    assert devolucao.valor_estornado == Decimal("129.90")
    assert chaleira.estoque == 5
    assert torradeira.estoque == 2


if __name__ == "__main__":
    main()