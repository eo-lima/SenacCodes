from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTabWidget,
    QVBoxLayout,
    QWidget
)
from estilo import(
    QSS,
    aguardando,
    botao,
    cabecalho,
    campo,
    icone,
    moeda,
    rotulo_erro,
    valor_digitado
)
import banco
from config import SALDO_INICIAL

import sys
CADASTRO, LOGIN, CONTA, OPERACOES = 0, 1, 2, 3
 
def _aba(widget):
    layout = QVBoxLayout(widget)
    layout.setContentsMargins(60,44,60,44)
    layout.setSpacing(10)
    return layout
 
class AbaCadastro(QWidget):
    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)
        cabecalho(layout, "banco.png", "Abrir conta", f"Toda conta nova começa com {moeda(SALDO_INICIAL)}")
        self.nome = campo(layout, "Nome completo", "Seu nome")
        self.email = campo(layout, "Email", "Seu email")
        self.senha = campo(layout, "Mínimo de 6 caracteres", senha=True)
        self.confirmar = campo(layout, "Confirmar senha", "Repita a senha", senha=True)
        self.confirmar.returnPressed.connect(self.cadastrar)
        self.erro = rotulo_erro(layout)
        self.addWidget(botao("Cadastrar", self.cadastrar))
        layout.addStretch(1)
    
    def cadastrar(self):
        nome = self.nome.text().strip()
        email = self.email.text().strip()
        senha = self.senha.text()

        if not nome or not email or not senha:
            self.erro.setText("Preencha todos os campo.")
            return
        if "@" not in email:
            self.erro.setText("Informe um email válido.")
            return
        if len(senha) < 6:
            self.erro.setText("A senha precisa de pelo menos 6 caracteres.")
            return
        if senha != self.confirmar.text():
            self.erro.setText("As senhas não são iguais.")
            return
        try:
            with aguardando():
                banco.cadastrar(email, nome, senha)
        except ErroBanco as e:
            self.erro.setText(str(e))
            return
        self.erro.clear()
        for entrada in (self.nome, self.email, self.senha, senha.confirmar):
            entrada.clear()
        QMessageBox.information(
            self, "Conta criada com sucesso",
            f"Seu saldo é {moeda(SALDO_INICIAL)}.\nFaça Login para continuar"
        )
        self.janela.login.preencher(email)
        self.janela.setCurrentIndex(LOGIN)

class AbaLogin(QWidget):
    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)
        
        cabecalho(layout, "banco.png", "Acesse sua conta", "Informe email e senha")
        self.email = campo(layout, "Email", "email@voce.com")
        self.senha = campo(layout, "Senha", "****", senha=True)
        self.senha.returnPressed.connect(self.entrar)
        mostrar = QCheckBox("Mostrar Senha")
        mostrar.toggled.connect(
            lambda ligado: self.senha.setEchoMode(
                QLineEdit.Normal if ligado else QLineEdit.Password
            )
        )
        layout.addWidget(mostrar)
        layout.addSpacing(10)
        self.erro = rotulo_erro(layout)
        layout.addWidget(botao("Entrar", self.entrar))
        layout.addStretch(1)
    def entrar(self):
        try:

        except:


       
 
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TMF")
    app.setFont(QFont("Segoe UI", 10))
    janela = Janela()
    janela.show()
 
if __name__ == "__main__":
    main()