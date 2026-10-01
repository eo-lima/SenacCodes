from models.pessoas import Pessoa
from models.subpessoas.cliente import Cliente
from models.subpessoas.vendedor import Vendedor
from views.console_view import ConsoleView


class PessoaController:
    def __init__(self, view=None):
        self.view = view or ConsoleView()

    def cadastrar_usuario(self):
        tipo = self.view.escolher_tipo_usuario()
        if tipo not in ("1", "2"):
            self.view.mostrar_mensagem("Opção Inválida.", "vermelho")
            return

        nome = self.view.digitar_texto("Digite o nome: ")
        cpf = self.view.digitar_inteiro("Digite o CPF: ")

        if tipo == "1":
            Pessoa.clientes.append(Cliente(nome, cpf))
            self.view.mostrar_mensagem("Cliente cadastrado!", "verde")
        else:
            Pessoa.vendedores.append(Vendedor(nome, cpf))
            self.view.mostrar_mensagem("Vendedor cadastrado!", "verde")

    def listar_usuarios(self):
        tipo = self.view.escolher_tipo_listagem()
        if tipo == "1":
            self.view.listar_pessoas("Clientes", Pessoa.clientes)
        elif tipo == "2":
            self.view.listar_pessoas("Vendedores", Pessoa.vendedores)
        else:
            self.view.mostrar_mensagem("Opção Inválida.", "vermelho")

    def exibir_comissao(self):
        nome = self.view.digitar_texto(
            "Digite o nome do vendedor que deseja ver seu total de comissão: "
        )
        vendedor = next(
            (pessoa for pessoa in Pessoa.vendedores if pessoa.nome == nome), None
        )
        if vendedor is None:
            self.view.mostrar_mensagem("Vendedor não encontrado.", "vermelho")
        else:
            self.view.mostrar_comissao(vendedor)

    def exibir_compras(self):
        nome = self.view.digitar_texto("Digite o nome do cliente: ")
        cliente = next(
            (pessoa for pessoa in Pessoa.clientes if pessoa.nome == nome), None
        )
        if cliente is None:
            self.view.mostrar_mensagem("Cliente não encontrado.", "vermelho")
        elif cliente.compras:
            self.view.mostrar_historico_compras(cliente)
        else:
            self.view.mostrar_mensagem(
                "Cliente com nenhuma compra registrada.", "vermelho"
            )
