from pessoas import Pessoa

class Cliente(Pessoa):

    compras = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def exibir_compras():
        nome_cliente = input("Digite o nome do cliente: ")
        cliente_encontrado = None
        for cliente in Pessoa.clientes:
            if nome_cliente == cliente.nome:
                cliente_encontrado = cliente
                break
        if cliente_encontrado == None:
            print("\033[31mCliente não encontrado.\033[0m")
        else:
            if len(cliente.compras) > 0:
                print(f"Histórico de Compras de {cliente.nome}: ")
                for compra in cliente.compras:
                    produtos_compra = compra[0]
                    valor_total = compra[1]
                    for i, produto in enumerate(produtos_compra):
                        print(f"Produto ({i+1}): {produto['produto']._nome}, Quantidade: {produto['quantidade']}")
                    print(f"Valor Total: R${valor_total}\n")
            else:
                print("\033[31mCliente com nenhuma compra registrada.\033[0m")


        