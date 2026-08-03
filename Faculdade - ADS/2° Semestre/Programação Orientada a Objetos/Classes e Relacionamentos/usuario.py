class Usuario:
    def __init__(self, nome, email, login, senha, perfil):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = senha
        self.perfil = perfil

    def logar(self, login, senha):
        if self.login == login and self.senha == senha:
            return True
        else:
            return False
        