from estoque import Estoque
from produtos import Produto

class Audio(Produto):

    comissao = 0.05
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cadastrar_produto():
        nome = input("Digite o nome do produto de Áudio: ")
        while True:
            try:
                preco = float(input("Digite o preço do produto de Áudio: "))
                break
            except ValueError:
                print("Digite apenas números.")
                continue
        while True:
            try:
                quantidade = int(input("Digite a quantidade do produto de Áudio: "))
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
        produto = Audio(nome, preco, quantidade, garantia)
        Estoque.lista_audio.append(produto)
        print("\033[32mProduto Cadastrado com Sucesso!\033[0m")

    