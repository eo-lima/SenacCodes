from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox #Ferramentas pra criar os componentes gráficos, como as janelas
from PySide6.QtCore import Qt #Faz alinhamento de texto dentro das labels que iremos criar
from PySide6.QtGui import QPixmap #Geramento de Imagem
import sys

class NomeImagemBotaoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerando Imagem")
        self.setGeometry(100, 100, 800, 400)
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        image_label = QLabel(self)
        pixmap = QPixmap("palmeiras.jpg")
        pixmap = pixmap.scaled(200,200)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        label = QLabel("Enzo Nogueira de Lima", self) #Criando uma label, já definindo um texto para dentro da aplicação
        label.setGeometry(50, 50, 300, 100)

        label.setStyleSheet("font-size: 23px; color: green; font-weight: bold; text-align: center;")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        layout.addWidget(image_label)
        self.setCentralWidget(central_widget)

        self.botao = QPushButton("Clique Aqui")
        self.botao.clicked.connect(self.clicou_botao)
        layout.addWidget(self.botao)

    def clicou_botao(self):
            QMessageBox.information(self, "VAI PALMEIRAS", "PALMEIRAS MAIOR DO BRASIL KKKKKKKKKKKKKK")

        

if __name__ == "__main__": #Só vai executar o comando e abrir a janela se for o arquivo principal
    app = QApplication(sys.argv) #Cria a aplicação
    window = NomeImagemBotaoWindow() #Passando os métodos que personalizamos
    window.show() #Mostra a janela
    sys.exit(app.exec()) #Abrir a aplicação e esperar uma interação do usuário