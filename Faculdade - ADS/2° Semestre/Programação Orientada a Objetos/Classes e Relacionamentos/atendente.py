from usuario import Usuario

class Atendente(Usuario):
    def __init__(self, nome, email, login, senha, perfil, matricula, ramal, turno):
        super().__init__(nome, email, login, senha, perfil)
        self.matricula = matricula
        self.ramal = ramal
        self.turno = turno
        self.emprestimos = []

    def logar(self):
        return super().logar()

    def cadastro_emprestimo(self, emprestimo):
        if self.logar() == True:
            self.emprestimos.append(emprestimo)