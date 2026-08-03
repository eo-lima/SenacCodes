from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, email, login, senha, perfil, cpf, nascimento, rg, endereco):
        super().__init__(nome, email, login, senha, perfil)
        self.cpf = cpf
        self.nascimento = nascimento
        self.rg = rg
        self.endereco = endereco