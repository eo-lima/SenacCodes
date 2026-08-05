class Usuario:
    def __init__(self, nome, email, login, senha, perfil):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = senha
        self.perfil = perfil
        self.loginperfil = "admin"
        self.senhaperfil = "1234"

    def logar(self):
        if self.login == self.loginperfil and self.senha == self.senhaperfil:
            return True
        else:
            return False
        