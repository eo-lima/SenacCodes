from estoque import Estoque
from pessoas import Pessoa
from produtos import Produto
from Subpessoas.cliente import Cliente
from Subpessoas.vendedor import Vendedor

class Venda:
    def __init__(self, produtos: list, cliente: Cliente, vendedor: Vendedor):
        self.produtos = produtos
        self.cliente = cliente
        self.vendedor = vendedor

    def realizar_venda():
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
                nomeproduto = input("Qual o nome do produto que será comprado? ")
                produto_encontrado = None
                for audio in Estoque.lista_audio:
                    if audio._nome == nomeproduto:
                        produto_encontrado = audio
                        tipo_produto = "Áudio"
                        break
                if produto_encontrado == None:
                    for eletroportatil in Estoque.lista_eletroportatil:
                        if eletroportatil._nome == nomeproduto:
                            produto_encontrado = eletroportatil
                            tipo_produto = "Eletroportatil"
                            break
                if produto_encontrado == None:
                    for linhabranca in Estoque.lista_linhabranca:
                        if linhabranca._nome == nomeproduto:
                            produto_encontrado = linhabranca
                            tipo_produto = "Linha Branca"
                            break
                if produto_encontrado == None:
                    for video in Estoque.lista_video:
                        if video._nome == nomeproduto:
                            produto_encontrado = video
                            tipo_produto = "Vídeo"
                            break
                if produto_encontrado == None:
                    print("\033[31mProduto não encontrado.\033[0m")
                else:
                    print(f"\n\033[32mInformações: \033[0m\n\nProduto: {produto_encontrado._nome}\nTipo de Produto: {tipo_produto}\nPreço: {produto_encontrado._preco}\nQuantidade: {produto_encontrado._quantidade}")
                    confirmar = input("Qual será a forma de pagamento? (1 - A vista, 2 - Parcelado)")

                
                    


            
