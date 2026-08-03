from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QLineEdit, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
import signal

from app import imagem_perfil
from app.usuario import Usuario

largurajanela = 700
alturajanela = 750
largura_foto = 380

class PainelImagem(QLabel):
    def __init__(self, caminho_imagem=imagem_perfil, parent: QWidget | None=None):
        super().__init__(parent)
        self.setObjectName("Imagem")
        self.setAlignment(Qt.AlignCenter)
        self._carregar(caminho_imagem)
    def _carregar(self, caminho) -> None:
        pixmap = QPixmap(str(caminho))
        if pixmap.isNull():
            self.setText(f"Imagem não encontrada:\n{caminho.name}")
            return
        self.setPixmap(
            pixmap.scaled(
                largurajanela // 2,
                alturajanela // 2,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation, 
            )
        )


class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("TelaPrincipal")
        self.setWindowTitle("Tela Principal")
        self.setFixedSize(largurajanela, alturajanela)

        layout = QVBoxLayout()
        layout.setContentsMargins(130,130,130,130)
        layout.addSpacing(10)

        self.painel_imagem = PainelImagem()

        nome = QLabel("Enzo Nogueira de Lima")
        nome.setAlignment(Qt.AlignCenter)
        nome.setStyleSheet("font-size: 32px; font-weight: bold;")
        barrinha = QLabel("___________________________________________________________________________________________")
        barrinha.setAlignment(Qt.AlignCenter)
        email = QLabel("enzolimacubo@gmail.com")
        email.setAlignment(Qt.AlignCenter)
        numero = QLabel("(67) 99136-2624")
        numero.setAlignment(Qt.AlignCenter)


        layout.addWidget(self.painel_imagem, 2)
        layout.addWidget(barrinha)
        layout.addWidget(nome)
        layout.addWidget(email)
        layout.addWidget(numero)



        self.setLayout(layout)
    
