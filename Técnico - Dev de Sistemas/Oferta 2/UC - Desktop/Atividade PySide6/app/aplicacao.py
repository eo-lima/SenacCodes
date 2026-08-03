import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from app.estilos import Cores, estilo
from app.tela_login import TelaLogin
from app.tela_principal import TelaPrincipal

class Aplicacao:
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._configurar_tema()

        self.janela = TelaLogin()
        self.janela_principal: TelaPrincipal | None = None
        self.janela.autenticado.connect(self._abrir_janela_principal)
    
    def _configurar_tema(self) -> None:
        self._app.setStyle("Fusion")
        self._app.setStyleSheet(estilo)

        paleta = self._app.palette()
        paleta.setColor(QPalette.PlaceholderText, QColor(Cores.placeholder))
        self._app.setPalette(paleta)

    def _abrir_janela_principal(self):
        self.tela_principal = TelaPrincipal()
        self.tela_principal.show()
        self.tela_login.close()
    
    def executar(self) -> int:
        self.janela.show()
        return self._app.exec()