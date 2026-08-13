import sys
from PyQt6.QtWidgets import QApplication, QDialog
# Importa a classe visual que você gerou no arquivo Cadastro.py
from Cadastro import Ui_Dialog

class MinhaTela(QDialog):
    def __init__(self):
        super().__init__()
        # Cria a instância da interface gerada
        self.ui = Ui_Dialog()
        # Configura a interface dentro desta janela (Dialog)
        self.ui.setupUi(self)
        
        # Exemplo: Como interagir com o botão que você criou
        self.ui.pushButton.clicked.connect(self.ao_clicar_no_botao)

    def ao_clicar_no_botao(self):
        # Pega o texto digitado nos campos
        email = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        print(f"Botão clicado! Email: {email} | Senha: {senha}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinhaTela()
    window.show()
    sys.exit(app.exec())