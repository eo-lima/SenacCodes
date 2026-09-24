from model.pessoas import Pessoa

class VendaController:

    def verificar_cliente(nomecliente):
        cliente_encontrado = None
        for cliente in Pessoa.clientes:
            if cliente.nome == nomecliente:
                cliente_encontrado = cliente
                return True
                break
        if cliente_encontrado == None:
            print("\033[31mCliente não encontrado.\033[0m")
            return False

    def verificar_vendedor(nomevendedor):
        vendedor_encontrado = None
        for vendedor in Pessoa.vendedores:
            if vendedor.nome == nomevendedor:
                vendedor_encontrado = vendedor
                return True
                break
        if vendedor_encontrado == None:
            print("\033[31mVendedor não encontrado.\033[0m")
            return False
    