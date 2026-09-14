from estoque import Estoque
from pessoas import Pessoa
from produtos import Produto
from Subpessoas.cliente import Cliente
from Subpessoas.vendedor import Vendedor

class Venda:
    def __init__(self, cliente: Cliente, vendedor: Vendedor, *produtos):
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = produtos

    def realizar_venda():

        produtos_compra = []

        nomecliente = input("Digite o nome do cliente: ")
        cliente_encontrado = None
        for cliente in Pessoa.clientes:
            if cliente.nome == nomecliente:
                cliente_encontrado = cliente
                break
        if cliente_encontrado == None:
            print("\033[31mCliente não encontrado.\033[0m")
        else:
            nomevendedor = input("Digite o nome do vendedor: ")
            vendedor_encontrado = None
            for vendedor in Pessoa.vendedores:
                if vendedor.nome == nomevendedor:
                    vendedor_encontrado = vendedor
                    break
            if vendedor_encontrado == None:
                print("\033[31mVendedor não encontrado.\033[0m")
            else:
                adicionar_produto = "1"
                while adicionar_produto == "1":
                    nomeproduto = input("Qual o nome do produto que será comprado? ")
                    produto_encontrado = None
                    for audio in Estoque.lista_audio:
                        if audio._nome == nomeproduto:
                            produto_encontrado = audio
                            produtos_compra.append(audio)
                            break
                    if produto_encontrado == None:
                        for eletroportatil in Estoque.lista_eletroportatil:
                            if eletroportatil._nome == nomeproduto:
                                produto_encontrado = eletroportatil
                                produtos_compra.append(eletroportatil)
                                break
                    if produto_encontrado == None:
                        for linhabranca in Estoque.lista_linhabranca:
                            if linhabranca._nome == nomeproduto:
                                produto_encontrado = linhabranca
                                produtos_compra.append(linhabranca)
                                break
                    if produto_encontrado == None:
                        for video in Estoque.lista_video:
                            if video._nome == nomeproduto:
                                produto_encontrado = video
                                while True:
                                    try:
                                        quantidade = input("Quantos produtos serão comprados?")
                                        if quantidade > video._quantidade:
                                            print("\033[31mNão é possível comprar mais produtos do que o disponível no estoque.\033[0m")
                                            break
                                        break
                                    except ValueError:
                                        print("Digite apenas números.")
                                        continue
                                produto = {"produto": video, "quantidade": quantidade}
                                produtos_compra.append(produto)
                                break
                    if produto_encontrado == None:
                        print("\033[31mProduto não encontrado.\033[0m")
                        break
                    else:
                        adicionar_produto = input("Deseja adicionar mais um produto a compra? (1 - Sim, 2 - Não)")

                if adicionar_produto == "2":
                    valor_total = 0
                    for produto in produtos_compra:
                        valor_total = valor_total + produto.preco
                    print(f"\033[32mInformações da Compra: \033[0m\nProdutos:\n")
