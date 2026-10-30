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

    def cadastrar_cliente(dados):
        cpf_encontrado = None
        for cliente in Pessoa.clientes:
            if dados["cpf"] == cliente.cpf:
                cpf_encontrado = cliente
        if cpf_encontrado is None:
            cliente = Cliente(dados["telefone"], dados["nome"], dados["cpf"])
            Pessoa.clientes.append(cliente)
            return "sucesso"
        else:
            return "erro_cpf"