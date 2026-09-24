from controller.vendacontroller import VendaController

class VendaView:

    def realizar_venda():
        nomecliente = input("Digite o nome do cliente: ")
        print(VendaController.verificar_cliente(nomecliente))
        if VendaController.verificar_cliente(nomecliente) == True:
            nomevendedor = input("Digite o nome do vendedor: ")
            VendaController.verificar_vendedor(nomevendedor)