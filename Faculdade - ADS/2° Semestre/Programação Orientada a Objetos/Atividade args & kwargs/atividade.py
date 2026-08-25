clientes = []
entregadores = []

class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def criar_usuario(tipo, **dados):
        tipo = tipo.lower()
        if tipo == "cliente":
            usuario = Cliente(**dados)
            clientes.append(usuario)
            return usuario
        elif tipo == "entregador":
            usuario = Entregador(**dados)
            entregadores.append(usuario)
            return usuario
        else:
            raise ValueError("Tipo não existente de usuário, apenas cliente e entregador.")

class Cliente(Pessoa):
    def __init__(self, endereco, ponto_de_referencia = "Sem ponto de referência", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endereco = endereco
        self.ponto_de_referencia = ponto_de_referencia


class Entregador(Pessoa):
    def __init__(self, veiculo, placa, avaliacao = "Sem avaliação", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.veiculo = veiculo
        self.placa = placa
        self.avaliacao = avaliacao

class Pedido:
    def __init__(self, cliente: Cliente, entregador: Entregador, *itens, **info):
        self.cliente = cliente
        self.entregador = entregador
        self.itens = itens
        self.info = info

    def registrar_pedido(self):
        resumo = f"Pedido de {self.cliente.nome}, Itens: {len(self.itens)}, [{', '.join(self.itens)}], Entregador: {self.entregador.nome}"
        if self.info:
            extras = " - " + ", ".join([f"{chave}: {valor}" for chave, valor in self.info.items()])
            resumo += extras
        return resumo
    
while True:
    print("============================")
    print("=           MENU            ")
    print("============================")
    print("1 - Criar Usuário")
    print("2 - Criar Entregador")
    print("3 - Registrar Pedido")
    print("4 - Sair")
    opcao = input("Digite a opção que deseja executar: ")
    match opcao:
        case "1":
            nome = input("Nome: ")
            email = input("Email :")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            ponto_de_referencia = input("Ponto de Referência: ") or "Sem ponto de referência"

            existe = None
            for c in clientes:
                if c.nome == nome:
                    existe = True
                    break
            if existe == True:
                print("Usuário já existente no sistema.")
                continue
            else:
                cliente = Pessoa.criar_usuario(
                    "cliente",
                    endereco=endereco,
                    nome=nome,
                    email=email,
                    telefone=telefone,
                    ponto_de_referencia=ponto_de_referencia
                )
                print("Cliente cadastrado com sucesso.")


        case "2":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            veiculo = input("Veículo: ")
            placa = input("Placa: ")
            avaliacao = input("Avaliação: ") or "Sem avaliação"

            existe = None
            for e in entregadores:
                if e.nome == nome:
                    existe = True
                    break
            if existe == True:
                print("Esse entregador já existe no sistema.")
                continue

            entregador = Pessoa.criar_usuario(
                "entregador",
                veiculo=veiculo,
                placa=placa,
                nome=nome,
                email=email,
                telefone=telefone
            )
            entregadores.append(entregador)
            print("Entregador cadastrado com sucesso.")

        case "3":
            clientenome = input("Nome do cliente: ")
            cliente_encontrado = None
            for c in clientes:
                if c.nome == clientenome:
                    cliente_encontrado = c
                    break
            if cliente_encontrado is None:
                print("Esse cliente não está cadastrado no sistema.")
                continue
            entregadornome = input("Nome do entregador: ")
            entregador_encontrado = None
            for e in entregadores:
                if e.nome == entregadornome:
                    entregador_encontrado = e
                    break
            if entregador_encontrado is None:
                print("Esse entregador não está cadastrado no sistema.")
                continue
            itenspedidos = []
            while True:
                itens = input("Digite o nome dos produtos (0 - Encerra o Loop): ")
                if itens == "0":
                    break
                itenspedidos.append(itens)

            pagamento = input("Qual a forma de pagamento?") or "Desconhecida"
            desconto = input("Quanto de desconto?") or "Sem desconto"
            pedido = Pedido(cliente_encontrado, entregador_encontrado, *itenspedidos, pagamento=pagamento, desconto=desconto)
            print(pedido.registrar_pedido())

        case "4":
            break