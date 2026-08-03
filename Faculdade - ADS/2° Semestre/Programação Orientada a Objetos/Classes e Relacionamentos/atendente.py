from usuario import Usuario

class Atendente(Usuario):
    def __init__(self, nome, email, login, senha, perfil, matricula, ramal, turno):
        super().__init__(nome, email, login, senha, perfil)
        self.matricula = matricula
        self.ramal = ramal
        self.turno = turno
        self.emprestimos = []

    def cadastro_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)