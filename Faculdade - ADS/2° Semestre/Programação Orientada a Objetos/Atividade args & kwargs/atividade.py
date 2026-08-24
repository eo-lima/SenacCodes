clientes = []
entregadores = []

class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

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
        print(f"Nome do Cliente:\n{self.cliente.nome}\n\nNúmero de Itens:\n{len(self.itens)}\n")
        print(f"Itens:")
        for item in self.itens:
            print(item)
        print("\nInformações: ")
        for chave, valor in self.info.items():
            print(f"{chave}: {valor}")
        print(f"Entregador: {self.entregador.nome}")

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
                
                


            else:
                print("Esse usuário não está registrado no sistema.")
                continue