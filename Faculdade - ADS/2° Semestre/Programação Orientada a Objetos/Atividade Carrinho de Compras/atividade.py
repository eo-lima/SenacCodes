produtos = []
clientes = []
carrinhos = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoCompra:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado!\n")

    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)
        print(f"Produto {produto.nome} removido com sucesso.\n")
    
    def calcular_preco(self) -> float:
        soma = 0
        for p in self.produtos:
            soma += p.preco
        return soma
    
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.carrinho = CarrinhoCompra()
    
    def finalizar_pedido(self):
        total = self.carrinho.calcular_preco()
        print(f"Pedido finalizado, valor total: R${total}")

while True:
    print("====================================")
    print("|               MENU               |")
    print("|1 - Cadastrar Produto             |")
    print("|2 - Cadastrar Cliente             |")
    print("|3 - Adicionar Produto ao Carrinho |")
    print("|4 - Remover Produto do Carrinho   |")
    print("|5 - Finalizar Compra              |")
    print("====================================")
    opcao = input("Digite qual operação deseja fazer: ")
    match opcao:
        case "1":
            nome = input("Digite o nome do produto: ")
            while True:
                try:
                    preco = int(input("Digite o preço do produto: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            produto = Produto(nome, preco)
            produtos.append(produto)
            print("Produto cadastrado com sucesso.")
        case "2":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            cliente = Cliente(nome, email)
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso.")
        case "3":
            if len(clientes) == 0:
                print("Nenhum cliente cadastrado.")
                continue
            if len(produtos) == 0:
                print("Nenhum produto cadastrado.")
                continue

            nome_cliente = input("Digite o nome do cliente: ")
            cliente_encontrado = None
            for cliente in clientes:
                if cliente.nome == nome_cliente:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado is None:
                print("Cliente não encontrado.")
                continue

            nome_produto = input("Digite o nome do produto: ")
            produto_encontrado = None
            for produto in produtos:
                if produto.nome == nome_produto:
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não encontrado.")
                continue

            carrinhos.append(cliente_encontrado.carrinho.adicionar_produto(produto_encontrado))
        case "4":
            if len(clientes) == 0:
                print("Não tem clientes cadastrados.")
                continue

            if len(produtos) == 0:
                print("Não tem produtos cadastrados.")
            
            nome_cliente = input("Digite o nome do cliente: ")
            cliente_encontrado = None
            for cliente in clientes:
                if cliente.nome == nome_cliente:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado is None:
                print("Cliente não encontrado.")
                continue
            
            nome_produto = input("Digite o nome do produto que deseja remover do carrinho: ")
            produto_encontrado = None
            for produto in cliente_encontrado.carrinho.produtos:
                if produto.nome == nome_produto:
                    produto_encontrado = produto
                    break
            if produto_encontrado is None:
                print("Produto não encontrado.")
                continue
            
            cliente_encontrado.carrinho.remover_produto(produto_encontrado)
        case "5":
            if len(clientes) == 0:
                print("Não foi cadastrado clientes.")
                continue
            
            nome_cliente = input("Digite o nome do cliente: ")
            cliente_encontrado = None
            for cliente in clientes:
                if cliente.nome == nome_cliente:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado is None:
                print("Cliente não encontrado no sistema.")
                continue
            
            print(f"Valor total do carrinho: R${cliente_encontrado.carrinho.calcular_preco()}\n")
            confirmar = input("Deseja confirmar o pedido?\n1 - Confirmar\n2 - Cancelar\n")
            match confirmar:
                case "1":
                    cliente_encontrado.finalizar_pedido()
                    continue
                case "2":
                    print("Pedido cancelado.")
                    continue
        