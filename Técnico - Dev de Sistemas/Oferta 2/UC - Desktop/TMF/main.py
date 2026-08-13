import sys

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
    QWidget,
)

import banco
from banco import ErroBanco
from config import SALDO_INICIAL
from estilo import (
    QSS,
    aguardando,
    botao,
    cabecalho,
    campo,
    icone,
    moeda,
    rotulo_erro,
    valor_digitado,
)

CADASTRO, LOGIN, CONTA, OPERACOES = 0, 1, 2, 3


def _aba(widget):
    layout = QVBoxLayout(widget)
    layout.setContentsMargins(60, 44, 60, 44)
    layout.setSpacing(0)
    return layout



class AbaCadastro(QWidget):
    """Abrir conta nova (liberada sem login)."""

    def __init__(self, janela):
        super().__init__()
        self.janela = janela         
        layout = _aba(self)

        cabecalho(layout, "piggy-bank.png", "Abrir conta",
                  f"Toda conta nova começa com {moeda(SALDO_INICIAL)}")

        self.nome = campo(layout, "Nome completo", "Seu nome")
        self.email = campo(layout, "E-mail", "voce@email.com")
        self.senha = campo(layout, "Senha", "mínimo 6 caracteres", senha=True)
        self.confirmar = campo(layout, "Confirmar senha", "repita a senha", senha=True)
        self.confirmar.returnPressed.connect(self.cadastrar)

        self.erro = rotulo_erro(layout)
        layout.addWidget(botao("Cadastrar", self.cadastrar))
        layout.addStretch(1)

    def cadastrar(self):
        nome = self.nome.text().strip()     
        email = self.email.text().strip()   
        senha = self.senha.text()  

        if not nome or not email or not senha:
            self.erro.setText("Preencha todos os campos.")
            return                  
        if "@" not in email:
            self.erro.setText("Informe um e-mail válido.")
            return
        if len(senha) < 6:
            self.erro.setText("A senha precisa ter pelo menos 6 caracteres.")
            return
        if senha != self.confirmar.text():
            self.erro.setText("As senhas não conferem.")
            return

        try:
            with aguardando():
                banco.cadastrar(email, nome, senha)
        except ErroBanco as e:      
            self.erro.setText(str(e))   
            return

        self.erro.clear()
        for entrada in (self.nome, self.email, self.senha, self.confirmar):
            entrada.clear()
        QMessageBox.information(
            self, "Conta criada",
            f"Conta criada com saldo de {moeda(SALDO_INICIAL)}.\nFaça login para continuar.",
        )
        self.janela.login.preencher(email)
        self.janela.setCurrentIndex(LOGIN)



class AbaLogin(QWidget):
    """Entrar numa conta existente (liberada sem login)."""

    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)

        cabecalho(layout, "bank.png", "Acesse sua conta", "Informe e-mail e senha")

        self.email = campo(layout, "E-mail", "voce@email.com")
        self.senha = campo(layout, "Senha", "••••", senha=True)
        self.senha.returnPressed.connect(self.entrar)

        mostrar = QCheckBox("Mostrar senha")
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
            with aguardando():
                conta = banco.autenticar(self.email.text().strip(), self.senha.text())
        except ErroBanco as e:
            self.erro.setText(str(e))
            return
        self.erro.clear()
        self.senha.clear()          
        self.janela.entrar(conta)   

    def preencher(self, email):
        self.email.setText(email)
        self.senha.setFocus()       

    def limpar(self):
        self.email.clear()
        self.senha.clear()
        self.erro.clear()



class AbaConta(QWidget):
    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)
        cabecalho(layout, "bank.png", "Minha conta", "Dados guardados no PlayFab")
        cartao = QFrame()
        cartao.setObjectName("cartao")   
        dados = QVBoxLayout(cartao)
        dados.setContentsMargins(28, 24, 28, 24)
        dados.setSpacing(4)
        legenda = QLabel("Saldo disponível")
        legenda.setObjectName("subtitulo")
        self.saldo = QLabel("R$ 0,00")   
        self.saldo.setObjectName("saldo")
        dados.addWidget(legenda)
        dados.addWidget(self.saldo)
        layout.addWidget(cartao)
        layout.addSpacing(24)

        self.titular = self._linha(layout, "Titular")
        self.email = self._linha(layout, "E-mail")
        self.identificador = self._linha(layout, "ID no PlayFab")
        layout.addSpacing(24)

        layout.addWidget(botao("Atualizar saldo", self.recarregar, secundario=True))
        layout.addSpacing(10)
        layout.addWidget(botao("Sair da conta", lambda: self.janela.sair(), secundario=True))
        layout.addStretch(1)

    @staticmethod
    def _linha(layout, rotulo):
        """Uma linha "Rótulo .......... valor"; devolve o rótulo do valor."""
        linha = QHBoxLayout()
        titulo = QLabel(rotulo)
        titulo.setObjectName("rotulo")
        valor = QLabel("-")
        linha.addWidget(titulo)
        linha.addStretch(1)
        linha.addWidget(valor)
        layout.addLayout(linha)
        layout.addSpacing(10)
        return valor

    def recarregar(self):
        if self.janela.conta is None:
            return
        try:
            with aguardando():
                banco.recarregar(self.janela.conta)
        except ErroBanco:
            pass
        self.atualizar()

    def atualizar(self):
        conta = self.janela.conta
        if conta is None:
            return
        self.saldo.setText(moeda(conta.saldo))
        self.titular.setText(conta.nome)
        self.email.setText(conta.email)
        self.identificador.setText(conta.playfab_id or "—")



class AbaOperacoes(QWidget):

    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)

        cabecalho(layout, "money-allocation.png", "Saque e transferência",
                  "Movimente o saldo da sua conta")

        self.valor_saque = campo(layout, "Valor do saque", "0,00")
        self.valor_saque.returnPressed.connect(self.sacar)
        layout.addWidget(botao("Sacar", self.sacar))
        layout.addSpacing(28)

        separador = QLabel("Transferência")
        separador.setObjectName("rotulo")
        layout.addWidget(separador)
        layout.addSpacing(10)

        self.destino = campo(layout, "E-mail de destino", "outra@email.com")
        self.valor_transf = campo(layout, "Valor", "0,00")
        self.valor_transf.returnPressed.connect(self.transferir)
        layout.addWidget(botao("Transferir", self.transferir))
        layout.addSpacing(10)

        self.erro = rotulo_erro(layout)
        layout.addStretch(1)

    def sacar(self):
        valor = valor_digitado(self.valor_saque.text())
        if valor is None:
            self.erro.setText("Valor inválido.")
            return
        try:
            with aguardando():
                banco.sacar(self.janela.conta, valor)
        except ErroBanco as e:
            self.erro.setText(str(e))
            return
        self.erro.clear()
        self.valor_saque.clear()
        self._concluido(f"Saque de {moeda(valor)} realizado.")

    def transferir(self):
        valor = valor_digitado(self.valor_transf.text())
        if valor is None:
            self.erro.setText("Valor inválido.")
            return
        try:
            with aguardando():
                nome_destino = banco.transferir(
                    self.janela.conta, self.destino.text().strip(), valor
                )
        except ErroBanco as e:
            self.erro.setText(str(e))
            return
        self.erro.clear()
        self.destino.clear()
        self.valor_transf.clear()
        self._concluido(f"{moeda(valor)} enviados para {nome_destino}.")

    def _concluido(self, mensagem):
        self.janela.conta_widget.atualizar()
        QMessageBox.information(
            self, "Operação concluída",
            f"{mensagem}\nSaldo: {moeda(self.janela.conta.saldo)}",
        )



class Janela(QTabWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa Eletrônico")
        self.setWindowIcon(QIcon(icone("bank.png", 64)))
        self.resize(700, 760)      
        self.setStyleSheet(QSS)

        self.conta = None

        self.login = AbaLogin(self)
        self.conta_widget = AbaConta(self)

        self.addTab(AbaCadastro(self), "Cadastro")
        self.addTab(self.login, "Login")
        self.addTab(self.conta_widget, "Conta")
        self.addTab(AbaOperacoes(self), "Saque e Transferência")
        self.setCurrentIndex(LOGIN)   

        self._liberar(False)          

    def _liberar(self, liberado):
        """Conta e operações só ficam acessíveis com login feito."""
        self.setTabEnabled(CONTA, liberado)
        self.setTabEnabled(OPERACOES, liberado)

    def entrar(self, conta):
        """Chamado pela aba de Login quando a autenticação dá certo."""
        self.conta = conta
        self.conta_widget.atualizar()
        self._liberar(True)
        self.setCurrentIndex(CONTA)   

    def sair(self):
        """Logout: esquece a conta e tranca tudo de novo."""
        self.conta = None
        self._liberar(False)
        self.login.limpar()
        self.setCurrentIndex(LOGIN)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Caixa Eletrônico")
    app.setFont(QFont("Segoe UI", 10))  

    janela = Janela()
    janela.show()    

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
