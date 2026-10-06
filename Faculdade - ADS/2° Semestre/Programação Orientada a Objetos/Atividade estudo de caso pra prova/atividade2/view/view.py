def menu():
    print("-------------")
    print("MENU")
    print("-------------")
    opcoes = {
        "1": "Cadastrar",
        "2": "Listar",
        "3": "Sair"
    }
    for numero, funcao in opcoes.items():
        print(f"{numero} - {funcao}")
    return input("Digite a opção que deseja: ")

def cadastrar():
    usuario = escolher_usuario()
    if usuario == "1":
        dados = cadastrar_cliente_view()
        return dados
    elif usuario == "2":
        pass

def cadastrar_cliente_view():
    nome = input("Digite o nome do cliente: ")
    while True:
        try:
            cpf = int(input("Digite o CPF do cliente: "))
            break
        except ValueError:
            print("Digite apenas números.")
            continue
    telefone = input("Digite o telefone do cliente: ")
    return {"tipo": "cliente", "nome": nome, "cpf": cpf, "telefone": telefone}

def escolher_usuario():
    return input("Digite qual usuário (1 - Cliente, 2 - Vendedor): ")

def listar():
    print("Listando...")

def opcao_invalida():
    print("Opção inválida.")    