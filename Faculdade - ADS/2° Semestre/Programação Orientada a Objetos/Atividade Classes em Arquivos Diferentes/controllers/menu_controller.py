from controllers.estoque_controller import EstoqueController
from controllers.pessoa_controller import PessoaController
from controllers.venda_controller import VendaController
from views.console_view import ConsoleView


class MenuController:
    def __init__(self):
        self.view = ConsoleView()
        self.pessoas = PessoaController(self.view)
        self.estoque = EstoqueController(self.view)
        self.vendas = VendaController(self.view)

    def executar(self):
        while True:
            opcao = self.view.exibir_menu()
            if opcao == "1":
                self.pessoas.cadastrar_usuario()
            elif opcao == "2":
                self.pessoas.listar_usuarios()
            elif opcao == "3":
                self.estoque.cadastrar_produto()
            elif opcao == "4":
                self.estoque.listar_produtos()
            elif opcao == "5":
                self.vendas.realizar_venda()
            elif opcao == "6":
                self.pessoas.exibir_comissao()
            elif opcao == "7":
                self.pessoas.exibir_compras()
            elif opcao == "8":
                self.view.mostrar_mensagem("Saindo...", "vermelho")
                break
            else:
                self.view.mostrar_mensagem("Opção Inválida.", "vermelho")
