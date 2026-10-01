from datetime import date

from model.devolucao import Devolucao
from model.venda import Venda
from view.terminal import TerminalView


class DevolucaoController:
    def __init__(self, view: TerminalView) -> None:
        self._view = view

    def executar(self, venda: Venda, data_devolucao: date) -> Devolucao | None:
        if self._view.exibir_menu() == 0:
            self._view.exibir_mensagem("Operação encerrada.")
            return None

        selecoes = self._view.selecionar_itens(venda)
        try:
            devolucao = Devolucao.registrar(venda, selecoes, data_devolucao)
        except ValueError as erro:
            self._view.exibir_mensagem(f"Devolução não registrada: {erro}")
            return None

        self._view.exibir_comprovante(devolucao)
        return devolucao