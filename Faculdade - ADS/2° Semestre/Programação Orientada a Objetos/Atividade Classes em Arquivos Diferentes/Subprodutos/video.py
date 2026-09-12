from estoque import Estoque
from produtos import Produto

class Video(Produto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comissao = 0.20

        def cadastrar_produto():
            nome = input("Digite o nome do produto de Vídeo: ")
            while True:
                try:
                    preco = float(input("Digite o preço do produto de Vídeo: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            while True:
                try:
                    quantidade = int(input("Digite a quantidade do produto de Vídeo: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            while True:
                try:
                    garantia = int(input("Digite a quantidade de dias de garantia: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            produto = Video(nome, preco, quantidade, garantia)
            Estoque.lista_video.append(produto)
            print("\033[32mProduto Cadastrado com Sucesso!\033[0m")