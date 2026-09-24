from model.estoque import Estoque
from model.produtos import Produto

class LinhaBranca(Produto):

    comissao = 0.15

    def __init__(self, consumo, classificacao, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumo = consumo
        self.classificacao = classificacao

    def cadastrar_produto():
        nome = input("Digite o nome do produto de Linha Branca: ")
        produto_encontrado = None
        for produto in Estoque.lista_audio:
            if nome == produto._nome:
                produto_encontrado = produto
                break
            else:
                for produto in Estoque.lista_eletroportatil:
                    if nome == produto._nome:
                        produto_encontrado = produto
                        break
                    else:
                        for produto in Estoque.lista_linhabranca:
                            if nome == produto._nome:
                                produto_encontrado = produto
                                break
                            else:
                                for produto in Estoque.lista_video:
                                    if nome == produto._nome:
                                        produto_encontrado = produto
                                        break
        if produto_encontrado == None:
            while True:
                try:
                    preco = float(input("Digite o preço do produto de Linha Branca: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            while True:
                try:
                    quantidade = int(input("Digite a quantidade do produto de Linha Branca: "))
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
                    consumo = int(input("Digite o consumo do produto: "))
                    break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            classificacao = input("Digite a classificação do produto: ")
            produto = LinhaBranca(consumo, classificacao, nome, preco, quantidade, garantia)
            Estoque.lista_linhabranca.append(produto)
            print("\033[32mProduto Cadastrado com Sucesso!\033[0m")
        else:
            print("\033[31mJá existe um produto com esse nome.\033[0m")
