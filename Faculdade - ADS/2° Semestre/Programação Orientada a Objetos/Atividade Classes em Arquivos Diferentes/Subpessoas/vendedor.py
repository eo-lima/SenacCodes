from pessoas import Pessoa

class Vendedor(Pessoa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._comissao = 0

    def mostrar_comissao():
        nome_vendedor = input("Digite o nome do vendedor que deseja ver seu total de comissão: ")
        vendedor_encontrado = None
        for vendedor in Pessoa.vendedores:
            if nome_vendedor == vendedor.nome:
                vendedor_encontrado = vendedor
                break
        if vendedor_encontrado == None:
            print("\033[31mVendedor não encontrado.\033[0m")
        else:
            print(f"Comissão de {vendedor.nome}: R${vendedor._comissao}")