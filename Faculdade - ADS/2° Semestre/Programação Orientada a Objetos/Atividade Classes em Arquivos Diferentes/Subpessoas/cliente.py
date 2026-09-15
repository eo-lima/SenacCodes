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
                i = 0
                for compra in cliente.compras:
                    if i > len(cliente.compras):
                        break
                    print(f"Produto: {compra[0][0]["produto"]._nome}, Quantidade: {compra[0][0]["quantidade"]}, Valor Total: R${cliente.compras[i][1]}\n")
                    i = i+1
            else:
                print("\033[31mCliente com nenhuma compra registrada.\033[0m")


        