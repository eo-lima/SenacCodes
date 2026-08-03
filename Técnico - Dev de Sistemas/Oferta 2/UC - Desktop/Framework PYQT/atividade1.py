from PySide6.QtWidgets import QApplication, QLabel, QMainWindow #Ferramentas pra criar os componentes gráficos, como as janelas
from PySide6.QtCore import Qt #Faz alinhamento de texto dentro das labels que iremos criar
import sys

#Estrutura de Inicialização da Aplicação
class NomeWindow(QMainWindow):
    def __init__(self):
        super().__init__() #Método Construtor do QMainWindow

        #Configuração Básica
        self.setWindowTitle("Nome") #Nome que vai ficar na aplicação desktop, no caso será "Hello World App"
        self.setGeometry(100, 100, 400, 200) #Definindo o tamanho da aplicação na tela e onde ela será aberta

        #Criando um texto e uma label
        label = QLabel("Enzo Nogueira de Lima", self) #Criando uma label, já definindo um texto para dentro da aplicação
        label.setGeometry(50, 50, 300, 100) #Definindo onde esse texto vai ficar dentro da janela e o tamanho da label

        #Estilo do Texto
        label.setStyleSheet("font-size: 23px; font-weight: bold; text-align: center; color: red")
        label.setAlignment(Qt.AlignCenter) #Definindo as características do texto, font-size determina o tamanho da fonte, font-weight define o tipo do texto, no caso negrito, e text-align define o alinhamento do texto, no caso ficará no centro

#Estrutura de Inicialização
if __name__ == "__main__": #Só vai executar o comando e abrir a janela se for o arquivo principal
    app = QApplication(sys.argv) #Cria a aplicação
    window = NomeWindow() #Passando os métodos que personalizamos
    window.show() #Mostra a janela
    sys.exit(app.exec()) #Abrir a aplicação e esperar uma interação do usuário
