from usuario import Usuario
from livro import Livro

class Bibliotecario(Usuario):
    def __init__(self, nome, email, login, senha, perfil, matricula, ramal, turno):
        super().__init__(nome, email, login, senha, perfil)
        self.matricula = matricula
        self.ramal = ramal
        self.turno = turno
        self.livros = []

    def logar(self):
        return super().logar()
    
    def cadastrar_livro(self, livro: Livro):
        if self.logar() == True:
            if livro not in self.livros:
                self.livros.append(livro)
        else:
            print("Não Logado.")

    def remover_livro(self, livro: Livro):
        if self.logar() == True:
            self.livros.pop(livro)
        else:
            print("Não Logado.")

    