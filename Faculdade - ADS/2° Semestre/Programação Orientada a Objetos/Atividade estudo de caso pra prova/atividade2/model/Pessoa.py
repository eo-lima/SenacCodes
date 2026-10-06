class Pessoa:

    clientes = []
    vendedores = []

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, telefone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telefone = telefone

class Vendedor(Pessoa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
