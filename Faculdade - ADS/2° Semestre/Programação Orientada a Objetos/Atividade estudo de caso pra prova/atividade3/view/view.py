def menu():
    print("========")
    print("Menu")
    print("========")
    opcoes = {
        "1": "Cadastrar",
        "2": "Listar",
        "3": "Sair",
    }
    for numero, funcao in opcoes.items():
        print(f"{numero} - {funcao}")
    return escolher_funcao()

def escolher_funcao():
    return input("Comando: ")

def cadastrar():
    usuario = escolher_usuario()
    if usuario == "1":
        dados = cadastrar_cliente_view()
        return dados


def escolher_usuario():
    return input("Qual usuário? (1 - Cliente, 2 - Vendedor)")

def cadastrar_cliente_view():
    nome = input("Digite o nome do cliente: ")
    while True:
        try:
            cpf = int(input("Digite o CPF do cliente: "))
        except ValueError:
            print("Digite apenas números.")
    telefone = input("Digite o telefone do cliente: ")
    return {"tipo": "cliente", "nome": nome, "cpf": cpf, "telefone": telefone}

def cadastro_confirmado():
    return print("Cadastro realizado com sucesso.")

def erro_cpf():
    return print("Esse CPF já existe dentro do sistema.")