def menu():
    print("===========\n- Menu\n===========")
    opcoes = {
        "1": "Cadastrar",
        "2": "Listar",
        "3": "Sair"
    }
    for numero, funcao in opcoes.items():
        print(f"{numero} - {funcao}")
    return input("Comando: ")

def escolher_usuario():
    return input("Qual usuário deseja? (1 - Tutor, 2 - Pet, 3 - Veterinário) ")

def cadastrar():
    usuario = escolher_usuario()

    if usuario == "1":
        dados = cadastrar_tutor_view()
        return {"tipo": "tutor", **dados}
    elif usuario == "2":
        dados = cadastrar_animal_view()
        return {"tipo": "cachorro", **dados}
    elif usuario == "3":
        dados = cadastrar_veterinario_view()
        return {"tipo": "veterinario", **dados}

def cadastrar_tutor_view():
    nome = input("Digite o nome do tutor: ")
    while True:
        try:
            cpf = int(input("Digite o CPF do tutor: "))
            break
        except ValueError:
            print("Digite apenas números: ")
            continue  
    return {"nome": nome, "cpf": cpf}

def cadastrar_animal_view():
    animal = escolher_animal()
    if animal == "1":
        dados = cadastrar_cachorro()
        return {**dados}

def escolher_animal():
    return input("Qual é o tipo de animal? (1 - Cachorro, 2 - Gato, 3 - Ave)")

def cadastrar_cachorro():
    nome = input("Digite o nome do cachorro: ")
    while True:
        try:
            peso = float(input("Digite o peso do cachorro: "))
            break
        except ValueError:
            print("Digite apenas números.")
            continue
    raca = input("Digite a raça do cachorro: ")
    cor = input("Digite a cor do cachorro: ")
    tutor = input("Digite o CPF do tutor: ")
    return {"nome": nome, "peso": peso, "raca": raca, "cor": cor, "tutor": int(tutor)}

def cadastrar_gato():
    nome = input("Digite o nome do gato: ")
    while True:
        try:
            peso = float(input("Digite o peso do gato: "))
            break
        except ValueError:
            print("Digite apenas números.")
            continue
    cor = input("Digite a cor do gato: ")
    tutor = input("Digite o CPF do tutor: ")
    return {"nome": nome, "peso": peso, "cor": cor, "tutor": tutor}

def cadastrar_veterinario_view(): 
    nome = input("Digite o nome do veterinário: ")
    while True:
        try:
            cpf = int(input("Digite o CPF do veterinário: "))
            break
        except ValueError:
            print("Digite apenas números. ")
            continue
    especialidade = input("Digite a especialidade do veterinário: ")
    return {"nome": nome, "cpf": cpf, "especialidade": especialidade}

def listar_tutores_view(tutores):
    print(tutores)

def listar_pets_view(pets):
    print(pets)

def listar_veterinario_view(veterinarios):
    print(veterinarios)

def erro_cpf():
    return print("Esse CPF já foi registrado.")

def cadastro_confirmado():
    return print("Cadastro realizado com sucesso.")

def nome_existente():
    return print("Não é possível cadastrar animais com o mesmo nome.")

def tutor_nao_encontrado():
    return print("O tutor desse animal não foi encontrado no sistema.")