clientes = []
entregadores = []

class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def criar_usuario(tipo, **dados):
        if tipo == "1":
            Cliente.criar_usuario(**dados)

class Cliente(Pessoa):
    def __init__(self, endereco, ponto_de_referencia = "Sem ponto de referência", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endereco = endereco
        self.ponto_de_referencia = ponto_de_referencia

    def criar_usuario(tipo, **dados):
        cliente = Cliente(**dados)
        clientes.append(cliente)

class Entregador(Pessoa):
    def __init__(self, veiculo, placa, avaliacao = "Sem avaliação", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.veiculo = veiculo
        self.placa = placa
        self.avaliacao = avaliacao

    def criar_usuario(tipo, **dados):
        entregador = Entregador(**dados)
        entregadores.append(entregador)

class Pedido:
    def __init__(self, cliente: Cliente, entregador: Entregador, *itens, **info):
        self.cliente = cliente
        self.entregador = entregador
        self.itens = itens
        self.info = info

    def registrar_pedido(cliente, *itens, **info):
        resumo = f"Pedido de {cliente.nome}, Itens: {len(itens)}, [{', '.join(itens)}]"
        if info == True:
            extras = " - " + ", ".join([f"{chave}: {valor}" for chave, valor in info.items()])
            resumo += extras
        return resumo
    
while True:
    print("============================")
    print("=           MENU            ")
    print("============================")
    print("1 - Criar Usuário")
    print("2 - Registrar Pedido")
    print("3 - Sair")
    opcao = input("Digite a opção que deseja executar: ")
    match opcao:
        case "1":
            opcao = input("Digite qual tipo de usuário será criado (1 - Cliente, 2 - Entregador): ")
            if opcao == "1":
                nomeusuario = input("Digite o nome completo do usuário: ")
                existe = None
                for c in clientes:
                    if c.nome == nomeusuario:
                        existe = True
                        break
                if existe == True:
                    print("Usuário já existe com esse nome.")
                    continue
                emailusuario = input("Digite o email do usuário: ")
                existe = None
                for c in clientes:
                    if c.email == emailusuario:
                        existe = True
                        break
                if existe == True:
                    print("Usuário já existe com esse email.")
                    continue
                telefoneusuario = input("Digite o telefone do usuário: ")
                existe = None
                for c in clientes:
                    if c.telefone == telefoneusuario:
                        existe = True
                        break
                if existe == True:
                    print("Usuário já existe com esse telefone.")
                    continue
                enderecousuario = input("Digite o endereço do usuário: ")
                ponto_de_referencia = input("(Opcional) Digite o ponto de referência do seu usuário: ")
                cliente = Cliente(enderecousuario, ponto_de_referencia, nomeusuario, emailusuario, telefoneusuario)
                clientes.append(cliente)
                print("Usuário cadastrado com sucesso.")
        case "2":
            usuariopedido = input("Digite o nome do cliente que pediu: ")
            existe = None
            for c in clientes:
                if c.nome == usuariopedido:
                    existe = True
            if existe == True:
                itenspedidos = []
                while itens != 0:
                    itens = input("Digite o nome dos produtos que serão pedidos (0 - Cancela o Loop): ")
                    if itens != 0:
                        itenspedidos.append(itens)
                        continue
                    else:
                        break
            entregador = input("Digite o nome do entregador: ")
            existe = None
            for e in entregadores:
                if e.nome == entregador:
                    existe = True
                    break
            if existe == None:
                print("Entregador não encontrado no sistema.")
                continue
            
                
            else:
                print("Esse usuário não está registrado no sistema.")
                continue