from Subprodutos.audio import Audio
from Subprodutos.eletroportatil import Eletroportateis
from Subprodutos.linhabranca import LinhaBranca
from Subprodutos.video import Video
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
                            while True:
                                try:
                                    quantidade = int(input("Quantos produtos serão comprados?"))
                                    if quantidade > audio._quantidade:
                                        print("\033[31mNão é possível comprar mais produtos do que o disponível no estoque.\033[0m")
                                        break
                                    else:
                                        produto = {"produto": audio, "quantidade": quantidade}
                                        produtos_compra.append(produto)
                                        print("\033[32mProduto adicionado com sucesso!\033[0m")
                                        break
                                except ValueError:
                                    print("Digite apenas números.")
                                    continue
                    if produto_encontrado == None:
                        for eletroportatil in Estoque.lista_eletroportatil:
                            if eletroportatil._nome == nomeproduto:
                                produto_encontrado = eletroportatil
                                while True:
                                    try:
                                        quantidade = int(input("Quantos produtos serão comprados?"))
                                        if quantidade > eletroportatil._quantidade:
                                            print("\033[31mNão é possível comprar mais produtos do que o disponível no estoque.\033[0m")
                                            break
                                        else:
                                            produto = {"produto": eletroportatil, "quantidade": quantidade}
                                            produtos_compra.append(produto)
                                            print("\033[32mProduto adicionado com sucesso!\033[0m")
                                    except ValueError:
                                        print("Digite apenas números.")
                                        continue
                    if produto_encontrado == None:
                        for linhabranca in Estoque.lista_linhabranca:
                            if linhabranca._nome == nomeproduto:
                                produto_encontrado = linhabranca
                                while True:
                                    try:
                                        quantidade = int(input("Quantos produtos serão comprados?"))
                                        if quantidade > linhabranca._quantidade:
                                            print("\033[31mNão é possível comprar mais produtos do que o disponível no estoque.\033[0m")
                                            break
                                        else:
                                            produto = {"produto": linhabranca, "quantidade": quantidade}
                                            produtos_compra.append(produto)
                                            print("\033[32mProduto adicionado com sucesso!\033[0m")
                                            break
                                    except ValueError:
                                        print("Digite apenas números.")
                                        continue
                    if produto_encontrado == None:
                        for video in Estoque.lista_video:
                            if video._nome == nomeproduto:
                                produto_encontrado = video
                                while True:
                                    try:
                                        quantidade = int(input("Quantos produtos serão comprados?"))
                                        if quantidade > video._quantidade:
                                            print("\033[31mNão é possível comprar mais produtos do que o disponível no estoque.\033[0m")
                                            break
                                        else:
                                            produto = {"produto": video, "quantidade": quantidade}
                                            produtos_compra.append(produto)
                                            print("\033[32mProduto adicionado com sucesso!\033[0m")
                                            break
                                    except ValueError:
                                        print("Digite apenas números.")
                                        continue
                    if produto_encontrado == None:
                        print("\033[31mProduto não encontrado.\033[0m")
                        break
                    else:
                        adicionar_produto = input("Deseja adicionar mais um produto a compra? (1 - Sim, 2 - Não)")

                if adicionar_produto == "2":
                    if len(produtos_compra) > 0:
                        valor_total = 0
                        for produto in produtos_compra:
                            valor_total = valor_total + (produto["produto"]._preco * produto["quantidade"])
                        print(f"\033[32mInformações da Compra: \033[0m\n")
                        print("Produtos:\n")
                        for produto in produtos_compra:
                            print(f"Produto: {produto["produto"]._nome}\nQuantidade: {produto["quantidade"]}\n")
                        print(f"Valor Total: R${valor_total}\n")
                        loop_pagamento = True
                        while loop_pagamento:
                            forma_pagamento = input("Qual será a forma de pagamento? (1 - A vista, 2 - Parcelado)")
                            if forma_pagamento == "1":
                                valor_total = 0
                                for produto in produtos_compra:
                                    valor_total = valor_total + (produto["produto"]._preco * produto["quantidade"])
                                print(f"\033[32mInformações da Compra: \033[0m\n")
                                print("Produtos:\n")
                                for produto in produtos_compra:
                                    print(f"Produto: {produto["produto"]._nome}\nQuantidade: {produto["quantidade"]}\n")
                                print(f"Valor Total: R${valor_total}\n")
                            elif forma_pagamento == "2":
                                while True:
                                    try:
                                        parcelas = int(input("Quantas parcelas?"))
                                        if parcelas <= 1:
                                            print("\033[31mSó é possível parcelar a partir de 2 parcelas.\033[0m")
                                            continue
                                        else:
                                            valor_total = 0
                                            print(f"\033[32mExtrato da Compra: \033[0m\n")
                                            for produto in produtos_compra:
                                                valor_total = valor_total + (produto["produto"]._preco * produto["quantidade"])
                                            print(f"\033[32mInformações da Compra: \033[0m\n")
                                            print("Produtos:\n")
                                            for produto in produtos_compra:
                                                print(f"Produto: {produto["produto"]._nome}\nQuantidade: {produto["quantidade"]}\n")
                                            print(f"Sub-total: R${valor_total}\n")
                                            print(f"Acréscimo: R${(valor_total*10)/100}")
                                            print(f"Valor de cada parcela ({parcelas}): R${(valor_total + ((valor_total*10))/100)/parcelas}")
                                            print(f"Valor Total: {valor_total + ((valor_total*10)/100)}")
                                            break
                                    except ValueError:
                                        print("Digite apenas números.")
                            else:
                                print("\033[31mOpção Inválida.\033[0m")
                                continue
                            while True:
                                confirmar_compra = input("Confirmar Compra? (1 - Sim, 2 - Não)") 
                                if confirmar_compra == "1":
                                    for produto in produtos_compra:
                                        if produto["produto"] is Audio:
                                            vendedor._comissao = vendedor._comissao + (valor_total*audio.comissao)
                                        elif produto["produto"] is Eletroportateis:
                                            vendedor._comissao = vendedor._comissao + (valor_total*eletroportatil.comissao)
                                        elif produto["produto"] is LinhaBranca:
                                            vendedor._comissao = vendedor._comissao + (valor_total*linhabranca.comissao)
                                        else:
                                            vendedor._comissao = vendedor._comissao + (valor_total*Video.comissao)
                                    historico = [produtos_compra, valor_total]
                                    cliente.compras.append(historico)
                                    for produto in produtos_compra:
                                        produto["produto"]._quantidade = produto["produto"]._quantidade - produto["quantidade"]
                                    print("\033[32mCompra concluída com sucesso!\033[0m")
                                    loop_pagamento = False
                                    break
                                else:
                                    print("\033[31mCompra cancelada.\033[0m")
                                    loop_pagamento = False
                                    break