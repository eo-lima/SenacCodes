from usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self, nome, email, login, senha, perfil, matricula, ramal, turno):
        super().__init__(nome, email, login, senha, perfil)
        self.matricula = matricula
        self.ramal = ramal
        self.turno = turno
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.pop(livro)

    