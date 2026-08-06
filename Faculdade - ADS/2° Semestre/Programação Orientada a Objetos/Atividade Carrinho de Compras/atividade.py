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
        self.produtos.pop(produto)
        print(f"Produto removido com sucesso!\n")
    
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
            nome = input("Digite o nome do cliente: ")
            for cliente in clientes:
                if cliente == cliente.nome:
                    produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                    for produto in produtos:
                        if produto == produto.nome:
                                    
        case "4":
            remover = input("Digite o nome do produto que deseja retirar do carrinho: ")
            if remover in CarrinhoCompra.produtos:
                CarrinhoCompra.remover_produto(remover)
            else:
                print("Produto não encontrado dentro do carrinho.")
    # case "5":
        