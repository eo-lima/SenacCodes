from estoque import Estoque
from produtos import Produto

class Eletroportateis(Produto):
    def __init__(self, voltagem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voltagem = voltagem
        self.comissao = 0.10

    def cadastrar_produto():
        nome = input("Digite o nome do produto Eletroportatil: ")
        while True:
            try:
                preco = float(input("Digite o preço do produto Eletroportatil: "))
                break
            except ValueError:
                print("Digite apenas números.")
                continue
        while True:
            try:
                quantidade = int(input("Digite a quantidade do produto Eletroportatil: "))
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
        while True:
            try:
                voltagem = int(input("Digite a voltagem do produto: "))
                break
            except ValueError:
                print("Digite apenas números.")
                continue
        produto = Eletroportateis(voltagem, nome, preco, quantidade, garantia)
        Estoque.lista_eletroportatil.append(produto)
        print("\033[32mProduto Cadastrado com Sucesso!\033[0m")