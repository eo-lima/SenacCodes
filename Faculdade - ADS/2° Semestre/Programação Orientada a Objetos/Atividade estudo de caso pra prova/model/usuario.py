class Usuario:

    tutores = []
    veterinarios = []

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Tutor(Usuario):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pets = []
        
class Veterinario(Usuario):
    def __init__(self, especialidade, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.especialidade = especialidade
