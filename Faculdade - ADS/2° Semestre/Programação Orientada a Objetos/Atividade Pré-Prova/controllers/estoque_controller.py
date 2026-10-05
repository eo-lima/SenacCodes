from models.estoque import Estoque
from models.subprodutos.audio import Audio
from models.subprodutos.eletroportatil import Eletroportateis
from models.subprodutos.linhabranca import LinhaBranca
from models.subprodutos.video import Video
from views.console_view import ConsoleView


class EstoqueController:
    def __init__(self, view=None):
        self.view = view or ConsoleView()
        self.tipos_produto = {
            "1": (Audio, Estoque.lista_audio, "produto de Áudio"),
            "2": (
                Eletroportateis,
                Estoque.lista_eletroportatil,
                "produto Eletroportátil",
            ),
            "3": (LinhaBranca, Estoque.lista_linhabranca, "produto de Linha Branca"),
            "4": (Video, Estoque.lista_video, "produto de Vídeo"),
        }

    def cadastrar_produto(self):
        tipo = self.view.escolher_tipo_produto(cadastro=True)
        configuracao = self.tipos_produto.get(tipo)
        if configuracao is None:
            self.view.mostrar_mensagem("Opção Inválida.", "vermelho")
            return

        classe, lista, descricao = configuracao
        nome = self.view.digitar_texto(f"Digite o nome do {descricao}: ")
        if Estoque.buscar_produto(nome) is not None:
            self.view.mostrar_mensagem(
                "Já existe um produto com esse nome.", "vermelho"
            )
            return

        preco = self.view.digitar_decimal(f"Digite o preço do {descricao}: ")
        quantidade = self.view.digitar_inteiro(
            f"Digite a quantidade do {descricao}: "
        )
        garantia = self.view.digitar_inteiro(
            "Digite a quantidade de dias de garantia: "
        )

        if classe is Eletroportateis:
            produto = classe(
                self.view.digitar_inteiro("Digite a voltagem do produto: "),
                nome,
                preco,
                quantidade,
                garantia,
            )
        elif classe is LinhaBranca:
            consumo = self.view.digitar_inteiro("Digite o consumo do produto: ")
            classificacao = self.view.digitar_texto(
                "Digite a classificação do produto: "
            )
            produto = classe(
                consumo, classificacao, nome, preco, quantidade, garantia
            )
        else:
            produto = classe(nome, preco, quantidade, garantia)

        lista.append(produto)
        self.view.mostrar_mensagem("Produto Cadastrado com Sucesso!", "verde")

    def listar_produtos(self):
        tipo = self.view.escolher_tipo_produto(cadastro=False)
        configuracao = self.tipos_produto.get(tipo)
        if configuracao is None:
            self.view.mostrar_mensagem("Opção Inválida.", "vermelho")
            return
        _, lista, _ = configuracao
        self.view.listar_produtos(lista, tipo)
